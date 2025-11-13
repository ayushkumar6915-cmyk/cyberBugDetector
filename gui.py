import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys

# FPDF ki ab zarurat nahi hai, isliye hata diya gaya hai.

# Correct package import handling for 'src'
# Yeh logic ensure karega ki 'analyze_file' sahi se import ho jaaye.
try:
    from src.analyzer import analyze_file
except ImportError:
    # Fallback mechanism for development environments
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    sys.path.append(project_root)
    
    try:
        from src.analyzer import analyze_file
    except ImportError as e:
        # Dummy function agar analyzer load nahi ho paya
        print(f"Error importing analyzer: {e}")
        def analyze_file(path):
            return "ANALYSIS FAILED: Could not load the analyzer module."


class CyberBugDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Cyber Bug Detector")

        # --- GUI Components Setup ---
        self.result_text = tk.Text(master, wrap='word', height=20, width=80)
        self.result_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.scan_button = tk.Button(master, text="Scan File", command=self.scan_file, bg='green', fg='white')
        self.scan_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.clear_button = tk.Button(master, text="Clear Report", command=self.clear_report, bg='gray', fg='white')
        self.clear_button.grid(row=1, column=1, padx=10, pady=10)

        self.file_path = ""
        self.analysis_output = "" 

    def clear_report(self):
        """Clears the text area."""
        self.result_text.delete('1.0', tk.END)
        messagebox.showinfo("Clear", "Report cleared.")

    def scan_file(self):
        """Opens file dialog, runs analysis, and displays result."""
        
        # 1. File Selection
        self.file_path = filedialog.askopenfilename(
            title="Select File to Analyze",
            filetypes=(("All files", "*.*"), ("Python files", "*.py"))
        )
        
        if not self.file_path:
            return

        # Clear previous results and display status
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, f"--- Analyzing: {os.path.basename(self.file_path)} ---\n")

        try:
            # 2. Run Analysis
            self.analysis_output = analyze_file(self.file_path) 
            
            # 3. Display Result (Success)
            self.result_text.insert(tk.END, self.analysis_output)
            
            messagebox.showinfo("Scan Complete", "Analysis finished. Result displayed on screen.")

        except Exception as e:
            error_message = f"An error occurred during scan or analysis: {e}"
            self.result_text.insert(tk.END, f"\nERROR: {error_message}")
            messagebox.showerror("Scan Error", error_message)

# generate_pdf_report function yahan se hata diya gaya hai.

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberBugDetectorApp(root)
    root.mainloop()