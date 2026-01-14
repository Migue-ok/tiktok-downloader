#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de limpieza de archivos de build
Elimina archivos temporales y de compilación
"""

import os
import shutil
import sys
from pathlib import Path


def get_size_mb(path):
    """Obtener tamaño de un directorio en MB"""
    total = 0
    try:
        for entry in Path(path).rglob('*'):
            if entry.is_file():
                try:
                    total += entry.stat().st_size
                except (PermissionError, OSError) as e:
                    # Ignorar archivos a los que no tenemos acceso
                    continue
    except Exception:
        pass
    return total / (1024 * 1024)


def clean_directory(path, description):
    """Limpiar un directorio"""
    if os.path.exists(path):
        size_mb = get_size_mb(path)
        try:
            shutil.rmtree(path)
            print(f"  ✅ Eliminado {description} ({size_mb:.1f} MB)")
            return size_mb
        except Exception as e:
            print(f"  ❌ Error eliminando {description}: {e}")
            return 0
    else:
        print(f"  ℹ️  {description} no existe (ya limpio)")
        return 0


def clean_file_pattern(directory, pattern, description):
    """Limpiar archivos que coincidan con un patrón"""
    count = 0
    size_mb = 0
    
    try:
        for file in Path(directory).rglob(pattern):
            if file.is_file():
                size_mb += file.stat().st_size / (1024 * 1024)
                file.unlink()
                count += 1
        
        if count > 0:
            print(f"  ✅ Eliminados {count} {description} ({size_mb:.1f} MB)")
        return size_mb
    except Exception as e:
        print(f"  ❌ Error limpiando {description}: {e}")
        return 0


def main():
    """Función principal"""
    print("╔" + "="*58 + "╗")
    print("║  🧹 LIMPIADOR DE ARCHIVOS DE BUILD                      ║")
    print("║  Elimina archivos temporales y de compilación          ║")
    print("╚" + "="*58 + "╝\n")
    
    # Cambiar al directorio Youtube si existe
    if not os.path.exists('build') and os.path.exists('Youtube'):
        os.chdir('Youtube')
        print("📁 Cambiando a directorio Youtube/\n")
    
    print("🧹 Iniciando limpieza...\n")
    
    total_cleaned = 0
    
    # Directorios de PyInstaller
    print("📦 Limpiando directorios de PyInstaller:")
    total_cleaned += clean_directory('build', 'directorio build/')
    total_cleaned += clean_directory('dist', 'directorio dist/')
    
    # Archivos de Python
    print("\n🐍 Limpiando archivos de Python:")
    total_cleaned += clean_directory('__pycache__', '__pycache__/')
    total_cleaned += clean_file_pattern('.', '*.pyc', 'archivos .pyc')
    total_cleaned += clean_file_pattern('.', '*.pyo', 'archivos .pyo')
    
    # Archivos de spec generados
    print("\n📋 Limpiando archivos .spec generados:")
    spec_files = ['Youtube_multifile.spec']
    for spec_file in spec_files:
        if os.path.exists(spec_file):
            try:
                size = os.path.getsize(spec_file) / (1024 * 1024)
                os.remove(spec_file)
                print(f"  ✅ Eliminado {spec_file} ({size:.3f} MB)")
                total_cleaned += size
            except Exception as e:
                print(f"  ❌ Error eliminando {spec_file}: {e}")
    
    # Archivos temporales
    print("\n🗑️  Limpiando archivos temporales:")
    temp_patterns = [
        ('*.log', 'archivos de log'),
        ('*.tmp', 'archivos temporales'),
        ('*~', 'archivos de backup'),
    ]
    
    for pattern, description in temp_patterns:
        total_cleaned += clean_file_pattern('.', pattern, description)
    
    # Archivos de verificación generados
    print("\n📄 Limpiando archivos de verificación:")
    verification_files = [
        'SHA256SUMS.txt',
        'BUILD_INFO.json',
        'build_info.txt',
    ]
    
    for file in verification_files:
        if os.path.exists(file):
            try:
                size = os.path.getsize(file) / (1024 * 1024)
                os.remove(file)
                print(f"  ✅ Eliminado {file} ({size:.3f} MB)")
                total_cleaned += size
            except Exception as e:
                print(f"  ❌ Error eliminando {file}: {e}")
    
    # Resultado final
    print("\n" + "="*60)
    print(f"✅ Limpieza completada")
    print(f"📊 Espacio liberado: {total_cleaned:.1f} MB")
    print("="*60)
    
    if total_cleaned > 0:
        print("\n💡 Ahora puedes ejecutar un build limpio:")
        print("   python build_multifile.py")
    else:
        print("\n✨ El directorio ya estaba limpio")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Limpieza cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
