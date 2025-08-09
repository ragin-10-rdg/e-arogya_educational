"""
Setup script for E-Arogya Backend
Run this script to set up the Django backend with all health content
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and print the result"""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ SUCCESS")
        if result.stdout:
            print("Output:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ ERROR")
        print("Error:", e.stderr)
        return False

def main():
    """Main setup function"""
    print("🏥 E-Arogya Backend Setup")
    print("=" * 50)
    
    # Change to backend directory
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(backend_dir)
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("Failed to install requirements. Please install manually:")
        print("pip install -r requirements.txt")
        return
    
    # Make migrations
    if not run_command("python manage.py makemigrations", "Creating database migrations"):
        print("Failed to create migrations")
        return
    
    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        print("Failed to run migrations")
        return
    
    # Create superuser (optional)
    print("\n" + "="*50)
    print("Creating Django superuser (optional)")
    print("You can skip this and create it later with: python manage.py createsuperuser")
    create_superuser = input("Create superuser now? (y/n): ").lower().strip()
    
    if create_superuser == 'y':
        run_command("python manage.py createsuperuser", "Creating superuser")
    
    # Populate health content
    if not run_command("python manage.py shell < populate_health_content.py", "Populating health content"):
        print("Failed to populate content. You can run it manually later:")
        print("python manage.py shell < populate_health_content.py")
    
    print("\n" + "🎉" * 20)
    print("E-Arogya Backend Setup Complete!")
    print("🎉" * 20)
    print("\nNext steps:")
    print("1. Start the development server: python manage.py runserver")
    print("2. Access admin panel: http://127.0.0.1:8000/admin/")
    print("3. API endpoints: http://127.0.0.1:8000/api/")
    print("4. Test API: http://127.0.0.1:8000/api/categories/")

if __name__ == "__main__":
    main()
