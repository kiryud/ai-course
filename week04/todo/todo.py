import json
import os
from datetime import datetime

DATA_FILE = "todo.json"

def load_tasks():
    """todo.json 파일에서 할 일 목록을 불러옵니다."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """할 일 목록을 todo.json 파일에 저장합니다."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")

def add_task(tasks):
    """새로운 할 일을 추가합니다. (마감일 포함)"""
    task_content = input("추가할 할 일을 입력하세요: ").strip()
    if not task_content:
        print("할 일 내용은 비어 있을 수 없습니다.")
        return

    due_date_str = input("마감일을 입력하세요 (YYYY-MM-DD, 미입력 시 건너뜀): ").strip()
    
    due_date = None
    if due_date_str:
        try:
            # 입력된 날짜가 유효한지 확인
            datetime.strptime(due_date_str, "%Y-%m-%d")
            due_date = due_date_str
        except ValueError:
            print("날짜 형식이 잘못되었습니다. YYYY-MM-DD 형식으로 입력해주세요. 마감일 없이 저장합니다.")
            due_date = None

    tasks.append({
        "task": task_content,
        "completed": False,
        "due_date": due_date
    })
    save_tasks(tasks)
    print(f"'{task_content}'가 추가되었습니다.")

def get_sorted_tasks(tasks):
    """할 일 목록을 마감일 순(빠른 순)으로 정렬하여 반환합니다. 마감일이 없으면 맨 뒤로 보냅니다."""
    return sorted(
        tasks, 
        key=lambda x: (x["due_date"] is None, x["due_date"] if x["due_date"] else "")
    )

def view_tasks(tasks):
    """할 일 목록을 보여줍니다."""
    sorted_tasks = get_sorted_tasks(tasks)
    if not sorted_tasks:
        print("\n현재 할 일이 없습니다.")
        return []

    print("\n--- 할 일 목록 (마감일 순) ---")
    for i, task in enumerate(sorted_tasks, 1):
        status = "[V]" if task["completed"] else "[ ]"
        due = f" | 마감: {task['due_date']}" if task["due_date"] else ""
        print(f"{i}. {status} {task['task']}{due}")
    print("------------------------------")
    return sorted_tasks

def complete_task(tasks):
    """할 일을 완료 상태로 표시합니다."""
    sorted_tasks = view_tasks(tasks)
    if not sorted_tasks:
        return

    try:
        choice = int(input("완료 처리할 번호를 입력하세요: "))
        if 1 <= choice <= len(sorted_tasks):
            # 정렬된 목록에서 선택한 항목을 찾아 원본 목록에서 업데이트
            target_task = sorted_tasks[choice - 1]
            for task in tasks:
                if task == target_task:
                    task["completed"] = True
                    break
            save_tasks(tasks)
            print(f"{choice}번 할 일을 완료 처리했습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해야 합니다.")

def delete_task(tasks):
    """할 일을 삭제합니다."""
    sorted_tasks = view_tasks(tasks)
    if not sorted_tasks:
        return

    try:
        choice = int(input("삭제할 번호를 입력하세요: "))
        if 1 <= choice <= len(sorted_tasks):
            target_task = sorted_tasks[choice - 1]
            tasks.remove(target_task)
            save_tasks(tasks)
            print(f"'{target_task['task']}' 항목이 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해야 합니다.")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== TODO 관리 프로그램 ===")
        print("1. 할 일 추가")
        print("2. 목록 보기")
        print("3. 완료 표시")
        print("4. 삭제")
        print("5. 종료")
        
        choice = input("메뉴를 선택하세요 (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
