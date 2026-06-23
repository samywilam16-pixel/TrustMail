import flet as ft

def main(page: ft.Page):
    page.title = "TrustMail - Pro Store AI"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def show_main_app():
        page.clean()
        
        app_bar = ft.AppBar(
            title=ft.Text("TrustMail Pro Dashboard", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
            bgcolor=ft.colors.SURFACE_VARIANT,
            center_title=True
        )

        store_name = ft.TextField(label="Your Store Name", hint_text="e.g. New York Bakery")
        customer_name = ft.TextField(label="Recipient Name / Customer Name")
        topic = ft.TextField(label="What is this email about?", hint_text="e.g. Special Discount, Late Order")
        
        generated_email = ft.TextField(
            label="Generated Professional Email", 
            multiline=True, 
            min_lines=6, 
            read_only=True
        )

        def generate_email_logic(e):
            if not store_name.value or not topic.value:
                page.snack_bar = ft.SnackBar(ft.Text("Please fill Store Name and Topic!"))
                page.snack_bar.open = True
                page.update()
                return
                
            email_text = (
                f"Subject: Important Update from {store_name.value}\n\n"
                f"Dear {customer_name.value or 'Valued Customer'},\n\n"
                f"We are writing to you regarding {topic.value}. Our team at {store_name.value} "
                f"is dedicated to providing you with the best business experience possible.\n\n"
                f"If you have any further questions, please do not hesitate to reply to this email.\n\n"
                f"Best Regards,\n"
                f"Management Team\n"
                f"{store_name.value}"
            )
            generated_email.value = email_text
            page.update()

        gen_btn = ft.ElevatedButton(
            text="Generate Professional Email", 
            icon=ft.icons.AUTO_AWESOME,
            on_click=generate_email_logic,
            style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_600, color=ft.colors.WHITE)
        )

        page.add(
            app_bar,
            ft.Text("Welcome back, Store Owner! Create your emails below:", size=16),
            store_name,
            customer_name,
            topic,
            gen_btn,
            ft.Divider(),
            generated_email
        )
        page.update()

    def pay_success(e):
        page.snack_bar = ft.SnackBar(ft.Text("Payment Successful! Opening App..."))
        page.snack_bar.open = True
        page.update()
        show_main_app()

    pay_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.icons.LOCK_PERSON, size=50, color=ft.colors.BLUE_400),
                    ft.Text("TrustMail Premium", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Write Professional Emails for Your Business", size=14, color=ft.colors.GREY_400),
                    ft.Divider(),
                    ft.Text("Subscription Plan:", size=16, weight=ft.FontWeight.W_500),
                    ft.Text("$35.00 / Month", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_400),
                    ft.Text("• Unlimited AI Business Emails\n• Professional Templates\n• 24/7 Customer Support", size=14),
                    ft.Divider(),
                    ft.TextField(label="Credit Card Number", hint_text="XXXX XXXX XXXX XXXX", keyboard_type=ft.KeyboardType.NUMBER),
                    ft.ElevatedButton(
                        text="Pay $35 & Open App Automatically", 
                        icon=ft.icons.CREDIT_CARD,
                        on_click=pay_success,
                        style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_700, color=ft.colors.WHITE)
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
            padding=30,
            width=400,
        )
    )

    page.add(pay_card)

if __name__ == "__main__":
    ft.app(target=main)

