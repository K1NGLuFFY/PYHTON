"""
Batch Script Runner
==================

Run multiple Python scripts or commands in batch.
"""

import subprocess
import os
import sys
from typing import List, Dict, Any
import json
from datetime import datetime

class BatchScriptRunner:
    """Run multiple scripts or commands in batch."""
    
    def __init__(self, log_file: str = "batch_run.log"):
        self.log_file = log_file
        self.results = []
    
    def run_command(self, command: str, cwd: str = None) -> Dict[str, Any]:
        """Run a single command and return results."""
        start_time = datetime.now()
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                cwd=cwd
            )
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            result_data = {
                "command": command,
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
                "start_time": start_time.isoformat(),
                "duration": duration
            }
            
            self.results.append(result_data)
            return result_data
            
        except Exception as e:
            result_data = {
                "command": command,
                "success": False,
                "error": str(e),
                "start_time": start_time.isoformat(),
                "duration": 0
            }
            self.results.append(result_data)
            return result_data
    
    def run_batch(self, commands: List[str], cwd: str = None) -> List[Dict[str, Any]]:
        """Run multiple commands in sequence."""
        for command in commands:
            self.run_command(command, cwd)
        return self.results
    
    def run_python_scripts(self, scripts: List[str], cwd: str = None) -> List[Dict[str, Any]]:
        """Run multiple Python scripts."""
        commands = [f"{sys.executable} {script}" for script in scripts]
        return self.run_batch(commands, cwd)
    
    def save_results(self, filename: str = None) -> None:
        """Save results to JSON file."""
        output_file = filename or self.log_file
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def print_summary(self) -> None:
        """Print summary of batch execution."""
        successful = sum(1 for r in self.results if r['success'])
        total = len(self.results)
        
        print(f"\n=== Batch Execution Summary ===")
        print(f"Total commands: {total}")
        print(f"Successful: {successful}")
        print(f"Failed: {total - successful}")
        
        for i, result in enumerate(self.results, 1):
            status = "✓" if result['success'] else "✗"
            print(f"{i}. {status} {result['command']}")
            if not result['success'] and 'stderr' in result:
                print(f"   Error: {result['stderr'][:100]}...")

# Example usage
def example_batch_run():
    """Example of running batch scripts."""
    runner = BatchScriptRunner()
    
    # Example commands
    commands = [
        "python --version",
        "echo Hello from batch runner",
        "dir" if os.name == 'nt' else "ls -la"
    ]
    
    results = runner.run_batch(commands)
    runner.print_summary()
    runner.save_results("example_batch_results.json")
    
    return results

if __name__ == "__main__":
    example_batch_run()
