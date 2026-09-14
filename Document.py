import subprocess
import sys

def install_packages():
    packages = ['requests', 'urllib3']
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} از قبل نصب است")
        except ImportError:
            print(f"📦 در حال نصب {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} با موفقیت نصب شد")

# اجرای تابع نصب
install_packages()
