"""
Daily Task Management System
Organizes tasks into completed and incomplete categories
"""


class TaskManager:
    def __init__(self):
        self.checklist = []
        self.completed_tasks = []
        self.incomplete_tasks = []
    
    def add_task(self, task):
        """Add a task to the daily checklist"""
        if task not in self.checklist:
            self.checklist.append(task)
            print(f"✓ Added task: '{task}'")
        else:
            print(f"Task '{task}' already exists in checklist")
    
    def mark_completed(self, task):
        """Mark a task as completed"""
        if task in self.checklist:
            self.checklist.remove(task)
            if task not in self.completed_tasks:
                self.completed_tasks.append(task)
            print(f"✓ Task completed: '{task}'")
        else:
            print(f"Task '{task}' not found in checklist")
    
    def mark_incomplete(self, task):
        """Mark a task as incomplete"""
        if task in self.checklist:
            self.checklist.remove(task)
            if task not in self.incomplete_tasks:
                self.incomplete_tasks.append(task)
            print(f"✗ Task marked incomplete: '{task}'")
        else:
            print(f"Task '{task}' not found in checklist")
    
    def view_checklist(self):
        """Display current checklist"""
        print("\n" + "="*50)
        print("📋 TODAY'S CHECKLIST")
        print("="*50)
        if self.checklist:
            for i, task in enumerate(self.checklist, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in checklist")
        print()
    
    def view_completed(self):
        """Display completed tasks"""
        print("\n" + "="*50)
        print("✓ COMPLETED TASKS")
        print("="*50)
        if self.completed_tasks:
            for i, task in enumerate(self.completed_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No completed tasks")
        print()
    
    def view_incomplete(self):
        """Display incomplete tasks"""
        print("\n" + "="*50)
        print("✗ INCOMPLETE TASKS")
        print("="*50)
        if self.incomplete_tasks:
            for i, task in enumerate(self.incomplete_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No incomplete tasks")
        print()
    
    def end_day_summary(self):
        """Display end of day summary"""
        print("\n" + "="*50)
        print("📊 END OF DAY SUMMARY")
        print("="*50)
        total_tasks = len(self.completed_tasks) + len(self.incomplete_tasks)
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {len(self.completed_tasks)}")
        print(f"Incomplete: {len(self.incomplete_tasks)}")
        
        if total_tasks > 0:
            completion_rate = (len(self.completed_tasks) / total_tasks) * 100
            print(f"Completion rate: {completion_rate:.1f}%")
        print()


def main():
    """Main function to demonstrate the task management system"""
    manager = TaskManager()
    
    # Start of day - Create checklist
    print("🌅 START OF DAY - CREATING CHECKLIST")
    print("="*50)
    
    tasks = [
        "Complete Python project",
        "Review code",
        "Write documentation",
        "Test application",
        "Submit work"
    ]
    
    for task in tasks:
        manager.add_task(task)
    
    manager.view_checklist()
    
    # During the day - Complete some tasks
    print("\n📝 DURING THE DAY - COMPLETING TASKS")
    print("="*50)
    
    manager.mark_completed("Complete Python project")
    manager.mark_completed("Write documentation")
    manager.mark_incomplete("Test application")
    
    manager.view_checklist()
    
    # End of day - Review and organize
    print("\n🌙 END OF DAY - FINAL REVIEW")
    
    # Move remaining tasks to incomplete
    remaining_tasks = manager.checklist.copy()
    for task in remaining_tasks:
        manager.mark_incomplete(task)
    
    # Display final results
    manager.view_completed()
    manager.view_incomplete()
    manager.end_day_summary()


if __name__ == "__main__":
    main()
