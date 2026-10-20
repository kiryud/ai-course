import flet as ft
from logic import calculate_parking_fee

def main(page: ft.Page):
    page.title = "주차 요금 계산기"
    page.window.width = 360
    page.window.height = 600
    page.window.resizable = False

    # 데이터 저장용 리스트
    records = []

    # UI 컨트롤 정의
    content = ft.Column(expand=True)
    
    # --- 요금 계산기 화면용 컨트롤 ---
    entry_time_input = ft.TextField(label="입차 시각 (HH:MM)", hint_text="09:30", width=140)
    exit_time_input = ft.TextField(label="출차 시각 (HH:MM)", hint_text="10:30", width=140)
    error_text = ft.Text("", color=ft.Colors.RED, size=12)
    
    total_amount_text = ft.Text("총 합계: 0원", size=20, weight=ft.FontWeight.BOLD)
    items_list = ft.ListView(expand=True, spacing=10, padding=10)

    def update_total():
        total = sum(r['fee'] for r in records)
        total_amount_text.value = f"총 합계: {total:,}원"
        page.update()

    def delete_record(e):
        idx = int(e.control.data)
        records.pop(idx)
        refresh_list()

    def refresh_list():
        items_list.controls.clear()
        for i, r in enumerate(records):
            items_list.controls.append(
                ft.Row(
                    [
                        ft.Text(f"{r['entry']}~{r['exit']}\n({r['duration']})", expand=True, size=12),
                        ft.Text(f"{r['fee']:,}원", width=70, size=12, weight=ft.FontWeight.W_500),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color=ft.Colors.RED,
                            data=str(i),
                            on_click=delete_record,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            )
        update_total()
        page.update()


    def on_calculate(e):
        nonlocal records
        error_text.value = ""
        
        entry = entry_time_input.value.strip()
        exit_t = exit_time_input.value.strip()

        if not entry or not exit_t:
            error_text.value = "시간을 입력해주세요."
            page.update()
            return

        try:
            duration_str, fee = calculate_parking_fee(entry, exit_t)
            
            records.append({
                "entry": entry,
                "exit": exit_t,
                "duration": duration_str,
                "fee": fee
            })
            
            # 입력란 초기화
            entry_time_input.value = ""
            exit_time_input.value = ""
            
            refresh_list()

        except ValueError as ve:
            error_text.value = str(ve)
        except Exception:
            error_text.value = "형식이 올바르지 않습니다. (HH:MM)"
        
        page.update()

    def menu_button(label, on_click_fn):
        return ft.Button(
            content=ft.Text(label, size=11, max_lines=1, no_wrap=True),
            on_click=lambda e: on_click_fn(label),
            expand=True,
            height=32,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
                padding=0,
            ),
        )

    def show_screen(menu):
        if menu == '요금 계산기':
            page.title = menu
            content.controls = [
                ft.Container(
                    content=ft.Column([
                        ft.Text("주차 요금 계산기", size=24, weight=ft.FontWeight.BOLD),
                        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                        ft.Row([entry_time_input, exit_time_input], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Button(
                            content=ft.Text("계산하기", size=14),
                            on_click=on_calculate,
                            width=200,
                            height=40,
                        ),
                        error_text,
                        ft.Divider(height=20),
                        total_amount_text,
                        ft.Container(content=items_list, expand=True, border=ft.border.Border.all(1, ft.Colors.GREY_400), border_radius=10, padding=5),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20
                )
            ]
        elif menu == '기록 확인':
            page.title = menu
            content.controls = [
                ft.Container(
                    content=ft.Column([
                        ft.Text("기록 확인", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text("준비 중인 화면입니다.", size=16),
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True,
                )
            ]
        page.update()

    header = ft.Column([
        ft.Row([
            menu_button('요금 계산기', show_screen),
            menu_button('기록 확인', show_screen),
        ], spacing=0,),
    ], spacing=0,)

    page.add(
        header,
        content,
    )
    
    # 초기 화면 실행
    show_screen('요금 계산기')

if __name__ == "__main__":
    ft.run(main)

