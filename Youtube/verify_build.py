#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificación post-build
Verifica que el ejecutable esté correctamente construido
"""

import os
import sys
import hashlib
import json
from pathlib import Path


def calculate_sha256(filepath):
    """Calcular SHA256 de un archivo"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(4096), b''):
            sha256.update(block)
    return sha256.hexdigest()


def check_build_exists():
    """Verificar que el build existe"""
    dist_dir = Path('dist/ApayKuMedias')
    
    if not dist_dir.exists():
        print("❌ No se encontró el directorio de build: dist/ApayKuMedias")
        return False
    
    exe_file = dist_dir / 'ApayKuMedias.exe'
    if not exe_file.exists():
        print("❌ No se encontró el ejecutable: ApayKuMedias.exe")
        return False
    
    print("✅ Directorio de build encontrado")
    return True


def check_essential_files():
    """Verificar que los archivos esenciales existan"""
    dist_dir = Path('dist/ApayKuMedias')
    
    essential_files = [
        'ApayKuMedias.exe',
        'python*.dll',  # Patrón
        'base_library.zip',
    ]
    
    essential_dirs = [
        'yt_dlp',
    ]
    
    print("\n📋 Verificando archivos esenciales...")
    
    # Verificar ejecutable
    exe_file = dist_dir / 'ApayKuMedias.exe'
    if exe_file.exists():
        size_mb = exe_file.stat().st_size / (1024*1024)
        print(f"  ✅ ApayKuMedias.exe ({size_mb:.2f} MB)")
    else:
        print("  ❌ ApayKuMedias.exe - FALTANTE")
        return False
    
    # Verificar Python DLL
    python_dlls = list(dist_dir.glob('python*.dll'))
    if python_dlls:
        for dll in python_dlls:
            size_mb = dll.stat().st_size / (1024*1024)
            print(f"  ✅ {dll.name} ({size_mb:.2f} MB)")
    else:
        print("  ❌ python*.dll - FALTANTE")
        return False
    
    # Verificar base_library.zip
    base_lib = dist_dir / 'base_library.zip'
    if base_lib.exists():
        size_mb = base_lib.stat().st_size / (1024*1024)
        print(f"  ✅ base_library.zip ({size_mb:.2f} MB)")
    else:
        print("  ❌ base_library.zip - FALTANTE")
    
    # Verificar directorios esenciales
    print("\n📁 Verificando directorios esenciales...")
    for dir_name in essential_dirs:
        dir_path = dist_dir / dir_name
        if dir_path.exists() and dir_path.is_dir():
            file_count = len(list(dir_path.rglob('*')))
            print(f"  ✅ {dir_name}/ ({file_count} archivos)")
        else:
            print(f"  ❌ {dir_name}/ - FALTANTE")
    
    return True


def analyze_build_size():
    """Analizar tamaño del build"""
    dist_dir = Path('dist/ApayKuMedias')
    
    print("\n📊 Análisis de tamaño...")
    
    total_size = 0
    file_count = 0
    
    # Categorías de archivos
    categories = {
        'Ejecutable': 0,
        'DLLs': 0,
        'Python Modules': 0,
        'Libraries': 0,
        'Others': 0,
    }
    
    for item in dist_dir.rglob('*'):
        if item.is_file():
            size = item.stat().st_size
            total_size += size
            file_count += 1
            
            # Categorizar
            if item.suffix == '.exe':
                categories['Ejecutable'] += size
            elif item.suffix == '.dll':
                categories['DLLs'] += size
            elif item.suffix in ['.pyd', '.pyc']:
                categories['Python Modules'] += size
            elif item.suffix == '.zip':
                categories['Libraries'] += size
            else:
                categories['Others'] += size
    
    print(f"  Total de archivos: {file_count}")
    print(f"  Tamaño total: {total_size/(1024*1024):.2f} MB")
    
    print("\n  Desglose por categoría:")
    for category, size in categories.items():
        if size > 0:
            size_mb = size / (1024*1024)
            percentage = (size / total_size) * 100
            print(f"    {category}: {size_mb:.2f} MB ({percentage:.1f}%)")
    
    # Verificar si el tamaño es razonable
    total_mb = total_size / (1024*1024)
    if total_mb > 150:
        print(f"\n  ⚠️  Advertencia: El build es grande ({total_mb:.2f} MB)")
        print("     Considera optimizar más las exclusiones")
    elif total_mb < 40:
        print(f"\n  ⚠️  Advertencia: El build es muy pequeño ({total_mb:.2f} MB)")
        print("     Puede que falten dependencias importantes")
    else:
        print(f"\n  ✅ Tamaño del build es razonable ({total_mb:.2f} MB)")
    
    return total_size, file_count


def generate_checksums():
    """Generar checksums de archivos importantes"""
    dist_dir = Path('dist/ApayKuMedias')
    
    print("\n🔐 Generando checksums...")
    
    checksums = {}
    
    # Archivos para checksum
    important_files = [
        'ApayKuMedias.exe',
    ]
    
    for filename in important_files:
        filepath = dist_dir / filename
        if filepath.exists():
            sha256 = calculate_sha256(filepath)
            checksums[filename] = sha256
            print(f"  ✅ {filename}")
            print(f"     SHA256: {sha256}")
    
    # Guardar checksums
    checksum_file = dist_dir.parent / 'SHA256SUMS.txt'
    with open(checksum_file, 'w') as f:
        for filename, sha256 in checksums.items():
            f.write(f"{sha256}  {filename}\n")
    
    print(f"\n  📄 Checksums guardados en: {checksum_file}")
    
    return checksums


def check_console_mode():
    """Verificar que console=False esté configurado"""
    print("\n🚫 Verificando configuración de consola...")
    
    # Esto es más difícil de verificar sin ejecutar,
    # pero podemos verificar los spec files
    spec_files = ['Youtube_multifile.spec', 'media_downloader_advanced.spec']
    
    for spec_file in spec_files:
        if os.path.exists(spec_file):
            with open(spec_file, 'r') as f:
                content = f.read()
                if 'console=False' in content:
                    print(f"  ✅ {spec_file}: console=False")
                else:
                    print(f"  ⚠️  {spec_file}: console mode no especificado")
    
    print("  ℹ️  Para verificar completamente, ejecutar el .exe")


def generate_build_info():
    """Generar información del build"""
    dist_dir = Path('dist/ApayKuMedias')
    
    print("\n📝 Generando información del build...")
    
    total_size, file_count = analyze_build_size()
    
    build_info = {
        'build_date': __import__('datetime').datetime.now().isoformat(),
        'total_files': file_count,
        'total_size_mb': round(total_size / (1024*1024), 2),
        'executable_path': 'dist/ApayKuMedias/ApayKuMedias.exe',
        'python_version': sys.version.split()[0],
    }
    
    info_file = dist_dir.parent / 'BUILD_INFO.json'
    with open(info_file, 'w') as f:
        json.dump(build_info, f, indent=2)
    
    print(f"  📄 Información guardada en: {info_file}")
    
    return build_info


def print_distribution_instructions():
    """Imprimir instrucciones de distribución"""
    print("\n" + "="*60)
    print("📦 INSTRUCCIONES DE DISTRIBUCIÓN")
    print("="*60)
    
    print("""
1. Comprimir la carpeta completa:
   cd dist
   # Windows: Clic derecho > Enviar a > Carpeta comprimida
   # Linux/Mac: zip -r ApayKuMedias.zip ApayKuMedias/

2. Crear archivo README para usuarios:
   Incluir instrucciones básicas de uso

3. Opcional - Escanear con antivirus:
   - Subir a VirusTotal.com
   - Documentar resultados
   - Incluir en el README

4. Distribuir:
   - GitHub Releases
   - Google Drive / Dropbox
   - Tu sitio web

5. Incluir archivos de soporte:
   - SHA256SUMS.txt (verificación de integridad)
   - BUILD_INFO.json (información del build)
   - README con instrucciones de uso
""")


def main():
    """Función principal"""
    print("╔" + "="*58 + "╗")
    print("║  🔍 VERIFICADOR POST-BUILD                              ║")
    print("║  Verifica que el ejecutable esté correctamente         ║")
    print("║  construido y listo para distribución                  ║")
    print("╚" + "="*58 + "╝\n")
    
    # Cambiar al directorio Youtube si es necesario
    if not os.path.exists('dist') and os.path.exists('Youtube'):
        os.chdir('Youtube')
        print("📁 Cambiando a directorio Youtube/\n")
    
    # Verificaciones
    checks_passed = 0
    total_checks = 5
    
    # 1. Verificar que el build existe
    if check_build_exists():
        checks_passed += 1
    
    # 2. Verificar archivos esenciales
    if check_essential_files():
        checks_passed += 1
    
    # 3. Analizar tamaño
    analyze_build_size()
    checks_passed += 1
    
    # 4. Verificar console mode
    check_console_mode()
    checks_passed += 1
    
    # 5. Generar checksums y build info
    try:
        generate_checksums()
        generate_build_info()
        checks_passed += 1
    except Exception as e:
        print(f"⚠️  Error generando archivos: {e}")
    
    # Resultado final
    print("\n" + "="*60)
    print(f"📊 RESULTADO: {checks_passed}/{total_checks} verificaciones pasadas")
    print("="*60)
    
    if checks_passed == total_checks:
        print("\n✅ ¡Build verificado exitosamente!")
        print("   El ejecutable está listo para distribución\n")
        print_distribution_instructions()
        return 0
    else:
        print("\n⚠️  Algunas verificaciones fallaron")
        print("   Revisa los mensajes de error arriba\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
