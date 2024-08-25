import os

def calculate_metrics(code_dir_path):
    # Initialize metrics
    loc = 0  # Lines of Code
    ploc = 0  # Physical Lines of Code (ignoring blank lines and comment lines)
    comments = 0  # Comment lines

    for filename in os.listdir(code_dir_path):
        file_path = os.path.join(code_dir_path, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    lines = file.readlines()
                    loc += len(lines)
                    for line in lines:
                        stripped_line = line.strip()
                        if stripped_line.startswith("#"):
                            comments += 1
                        elif stripped_line:
                            ploc += 1
            except UnicodeDecodeError as e:
                print(f"Error reading file {file_path}: {e}")
            except Exception as e:
                print(f"An error occurred with file {file_path}: {e}")

    return loc, ploc, comments

def filter_files(code_dir_path, extensions):
    filtered_files = []
    for filename in os.listdir(code_dir_path):
        if any(filename.endswith(ext) for ext in extensions):
            filtered_files.append(filename)
    return filtered_files

def main():
    code_dir_path = r"C:\Users\SAMSUNG\OneDrive\Documents\FCatstagram"
    extensions = ['.py', '.html', '.css', '.js']  # Add more extensions as needed
    
    filtered_files = filter_files(code_dir_path, extensions)
    if not filtered_files:
        print("No files found with the specified extensions.")
        return
    
    loc, ploc, comments = calculate_metrics(code_dir_path)

    print(f"Total Files: {len(filtered_files)}")
    print(f"LOC (Lines of Code): {loc}")
    print(f"PLOC (Physical Lines of Code): {ploc}")
    print(f"Comments: {comments}")

if __name__ == "__main__":
    main()
