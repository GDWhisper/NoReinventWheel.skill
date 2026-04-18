#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NoReinventWheel 发布脚本
生成 dist 目录，包含中英文两个技能包压缩包
"""

import os
import zipfile
import shutil
from pathlib import Path


def create_skill_package(lang_code, lang_name):
    """
    创建单个语言版本的技能包
    
    Args:
        lang_code: 语言代码 ('zh' 或 'en')
        lang_name: 语言名称 ('NoReinventWheel_zh' 或 'NoReinventWheel_en')
    
    Returns:
        str: 生成的压缩包路径
    """
    # 项目根目录
    root_dir = Path(__file__).parent
    
    # 源文件路径
    skill_md_path = root_dir / lang_name / "SKILL.md"
    meta_json_path = root_dir / "_meta.json"
    scripts_dir = root_dir / "scripts"
    
    # 输出目录
    dist_dir = root_dir / "dist"
    dist_dir.mkdir(exist_ok=True)
    
    # 压缩包路径
    zip_path = dist_dir / f"{lang_name}.skill"
    
    print(f"正在打包 {lang_name}...")
    
    # 创建 zip 文件
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 添加 SKILL.md（放在 no-reinvent-wheel/ 目录下）
        if skill_md_path.exists():
            zipf.write(skill_md_path, "no-reinvent-wheel/SKILL.md")
            print(f"  ✓ 添加 no-reinvent-wheel/SKILL.md")
        else:
            raise FileNotFoundError(f"找不到文件: {skill_md_path}")
        
        # 添加 _meta.json（放在 no-reinvent-wheel/ 目录下）
        if meta_json_path.exists():
            zipf.write(meta_json_path, "no-reinvent-wheel/_meta.json")
            print(f"  ✓ 添加 no-reinvent-wheel/_meta.json")
        else:
            raise FileNotFoundError(f"找不到文件: {meta_json_path}")
        
        # 添加 scripts 目录及其内容（放在 no-reinvent-wheel/scripts/ 目录下）
        if scripts_dir.exists() and scripts_dir.is_dir():
            for file_path in scripts_dir.iterdir():
                if file_path.is_file():
                    arc_name = f"no-reinvent-wheel/scripts/{file_path.name}"
                    zipf.write(file_path, arc_name)
                    print(f"  ✓ 添加 no-reinvent-wheel/scripts/{file_path.name}")
        else:
            raise FileNotFoundError(f"找不到目录: {scripts_dir}")
    
    print(f"✓ 已生成: {zip_path}\n")
    return str(zip_path)


def main():
    """主函数"""
    print("=" * 60)
    print("NoReinventWheel 发布脚本")
    print("=" * 60)
    print()
    
    try:
        # 清理旧的 dist 目录
        dist_dir = Path(__file__).parent / "dist"
        if dist_dir.exists():
            print("清理旧的 dist 目录...")
            shutil.rmtree(dist_dir)
            print("✓ 清理完成\n")
        
        # 生成中文版本
        zh_path = create_skill_package('zh', 'NoReinventWheel_zh')
        
        # 生成英文版本
        en_path = create_skill_package('en', 'NoReinventWheel_en')
        
        # 输出总结
        print("=" * 60)
        print("发布完成！")
        print("=" * 60)
        print(f"\n生成的文件:")
        print(f"  📦 {zh_path}")
        print(f"  📦 {en_path}")
        print(f"\n每个压缩包包含:")
        print(f"  - SKILL.md (对应语种的技能文档)")
        print(f"  - _meta.json (元数据)")
        print(f"  - scripts/ (脚本目录)")
        print()
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        raise


if __name__ == "__main__":
    main()
