import os
import sys

def extract_logs(log_file, date):
    output_dir = "output"
    output_file = f"{output_dir}/output_{date}.txt"
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Use os.path.abspath to get the absolute path
    abs_log_file = os.path.abspath(log_file)
    print(f"Using absolute log file path: {abs_log_file}")
    
    try:
        # Check if the file exists
        if not os.path.exists(abs_log_file):
            print(f"❌ Log file {abs_log_file} does not exist!")
            return
        
        with open(abs_log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith(date):  # Efficient filtering
                    outfile.write(line)
        
        print(f"✅ Logs for {date} saved to {output_file}")
    
    except FileNotFoundError:
        print(f"❌ Error: Log file {abs_log_file} not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    log_file = r"C:/Users/Sunny/test_logs.log"  # Use forward slashes to avoid any path escape issues
    
    extract_logs(log_file, date)
