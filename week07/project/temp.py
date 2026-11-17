import flet as ft

def main(page: ft.Page):
    page.title = "예제"
    page.window.width = 360
    page.window.height = 600
    page.window.resizable = False

    def menu_button(label, on_click_fn):
        return ft.Button(
            content=ft.Text(
                label,
                size=11,
                max_lines=1,
                no_wrap=True,
            ),
            on_click=lambda e: on_click_fn(label),
            expand=True,
            height=32,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
                padding=0,
            ),
        )

    def show_screen(menu):
            if menu == '단위 변환기':
                page.title = menu
                content = ft.Column(expand=True)
                value = ft.TextField(label="값", value="", width=150)
                result_value = ft.TextField(label="값", value="", width=150, read_only=True)
                unit = ft.Dropdown(label="단위", value="cm", width=120,
                                    options=[
                                        ft.dropdown.Option("mm"),
                                        ft.dropdown.Option("cm"),
                                        ft.dropdown.Option("m"),
                                        ft.dropdown.Option("km"),
                                        ft.dropdown.Option("°C"),
                                        ft.dropdown.Option("°F"),
                                    ])
                notice = ft.Text(value="", color=ft.Colors.RED)
                items = ft.ListView(expand=True, spacing=4)
                content.controls = [
                    ft.Column([
                        ft.Row(controls=[value, unit], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text("↓"),
                        ft.Row(controls=[result_value, unit], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Button(content="실행", on_click=on_run, expand=True, width=180, height=30,
                                  bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                        notice,
                        items,
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ]
            elif menu == '숫자 맞히기':
                page.title = menu
                content.controls = [
                    ft.Column([
                        ft.Text("1부터 100 사이의 숫자를 맞힙니다."),
                        ft.Row([
                            ft.TextField(label="값", value="", width=180),
                            ft.Button(content="실행", on_click=on_run, expand=True, width=90, height=30,
                                                          bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                            ]),
                        ft.Text(result, size=16, weight=ft.FontWeight.BOLD),
                        ft.Text("시도 횟수"),
                        ft.TextField(value="", width=380, min_lines=5, max_lines=10, multiline=True),
                        ft.Button(content="새 게임", on_click=on_run, expand=True, width=380, height=30,
                                bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                    ], horizontal_alignment=ft.CrossAxisAlignment.START),
                ]
            elif menu == '학점 계산기':
                page.title = menu
                content.controls = []
            elif menu == '비밀번호 생성기':
                page.title = menu
                content.controls = []
            elif menu == '용돈 기입장':
                page.title = menu
                content.controls = []
    
            page.update()

    header = ft.Column([
        ft.Row([
            menu_button("단위 변환기", show_screen),
            menu_button("숫자 맞히기", show_screen),
            menu_button("학점 계산기", show_screen),
        ], spacing=0,),
        ft.Row([
            menu_button("비밀번호 생성기", show_screen),
            menu_button("용돈 기입장", show_screen),
        ], spacing=0,),
    ], spacing=0,)

    content = ft.Column(expand=True)
    value = ft.TextField(label="값", value="", width=150)
    result_value = ft.TextField(label="값", value="", width=150, read_only=True)
    unit = ft.Dropdown(label="단위", value="cm", width=120,
                       options=[
                           ft.dropdown.Option("mm"),
                           ft.dropdown.Option("cm"),
                           ft.dropdown.Option("m"),
                           ft.dropdown.Option("km"),
                           ft.dropdown.Option("°C"),
                           ft.dropdown.Option("°F"),
                        ])
    upper = ft.Checkbox(label="대문자 포함", value=True)
    result = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)
    notice = ft.Text(value="", color=ft.Colors.RED)
    items = ft.ListView(expand=True, spacing=4)


    def on_run(e):
        notice.value = ""
        if not value.value.strip():
            notice.value = "값을 입력합니다"
        else:
            result.value = f"{value.value} {unit.value}, 대문자 {upper.value}"
            items.controls.append(ft.Row(controls=[
                ft.Text(value=result.value, expand=True),
                ft.Button(content="삭제", data=len(items.controls), on_click=on_delete),
            ]))
        page.update()

    def on_delete(e):
        items.controls.pop(e.control.data)     # 버튼을 만들 때 data에 넣어 둔 번호
        for i, row in enumerate(items.controls):
            row.controls[1].data = i
        page.update()

    page.add(
        header,
        content,
    )







if __name__ == "__main__":
    ft.run(main)
