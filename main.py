from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
import random

class TelaPrincipal(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Lista de mensagens de apoio / carinho
        self.mensagens = [
            "Voce nao faz ideia de como o meu peito fica cheio de paz quando converso com voce. ❤️",
            "O seu jeito doce e a minha coisa favorita no mundo todinho. ✨",
            "Ate o meu dia mais cansativo fica leve e bom quando voce esta por perto.",
            "So de saber que tenho voce comigo ja me sinto o cara mais sortudo que existe. 👑",
            "Voce e o meu momento preferido de todos os dias.",
            "Com esse seu jeito carinhoso, voce me ganha de novo todos os dias."
        ]

        # Layout principal vertical
        layout = MDBoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Título Personalizado
        self.titulo = MDLabel(
            text="👑 Exclusivamente para vc Allya",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.9, 0.2, 0.4, 1),
            font_style="H5",
            size_hint_y=None,
            height=40
        )

        # Card Central (Mensagens de Apoio)
        card = MDCard(
            orientation='vertical',
            padding=20,
            spacing=15,
            size_hint=(1, 0.45),
            radius=[20, 20, 20, 20],
            elevation=4
        )

        self.label_frase = MDLabel(
            text="Toque no botao abaixo sempre que precisar de um carinho 💕",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Custom",
            text_color=(0.3, 0.3, 0.3, 1)
        )
        card.add_widget(self.label_frase)

        # Botão de Mensagens de Apoio
        self.btn_apoio = MDRaisedButton(
            text="💌 Mensagem de Apoio",
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.9, 0.2, 0.4, 1),
            on_release=self.mostrar_mensagem_apoio
        )
        card.add_widget(self.btn_apoio)

        # Card da IA Exclusiva
        ai_card = MDCard(
            orientation='vertical',
            padding=15,
            spacing=10,
            size_hint=(1, 0.35),
            radius=[15, 15, 15, 15],
            md_bg_color=(0.98, 0.95, 0.96, 1)
        )
        
        self.ai_resposta = MDLabel(
            text="🤖 Olá, Allya! Sou sua assistente pessoal exclusiva. Eu só obedeço às suas ordens. Como posso te ajudar hoje?",
            halign="center",
            font_style="Body2",
            theme_text_color="Custom",
            text_color=(0.3, 0.3, 0.3, 1)
        )
        ai_card.add_widget(self.ai_resposta)

        # Monta a tela
        layout.add_widget(self.titulo)
        layout.add_widget(card)
        layout.add_widget(ai_card)
        self.add_widget(layout)

    def mostrar_mensagem_apoio(self, instance):
        msg_sorteada = random.choice(self.mensagens)
        self.label_frase.text = msg_sorteada


class AppAllya(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        return TelaPrincipal()

if __name__ == "__main__":
    AppAllya().run()
