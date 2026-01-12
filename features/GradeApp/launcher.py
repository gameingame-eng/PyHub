import subprocess
import os

# Paths relative to your repository root
java_filename = os.path.join("features", "GradeApp", "grading.java")
java_classname = "grading"
# Updated lib path to ensure it's found from root
lib_path = os.path.join("features", "GradeApp", "lib", "xchart-3.8.8.jar")

def run_java():
    # Automatically handles Windows (;) vs Linux/macOS (:)
    separator = ";" if os.name == 'nt' else ":"
    classpath = f".{separator}{lib_path}"

    try:
        # 1. Compile
        print(f"Compiling {java_filename} from root...")
        subprocess.run(["javac", "-cp", classpath, java_filename], check=True)

        # 2. Run
        print(f"Running {java_classname}...")
        result = subprocess.run(
            ["java", "-cp", classpath, java_classname],
            capture_output=True,
            text=True
        )

        print("Output:\n", result.stdout)
        if result.stderr:
            print("Errors:\n", result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Java command failed: {e}")
    except FileNotFoundError:
        print("Error: JDK not found. Ensure 'javac' is in your PATH.")

run_java()
