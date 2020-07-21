import ui
import sound


class TTTView(ui.View):
    def __init__(self):
        self.player1_turn = 1
        self.player2_turn = -1
        self.turn = -1


    def take_turn(self):
        # Set alpha of player's turn label and rotate turn count
        if self.turn == 1:
            l1.alpha = 1
            l2.alpha = 0
            l3.alpha = 0
            l4.alpha = 0
        elif self.turn == -1:
            l1.alpha = 0
            l2.alpha = 1
            l3.alpha = 0
            l4.alpha = 0
        self.turn *=-1

    def button_tapped(self, sender):
        # Set player's image and sound effect
        if sender.image == self.start_image:
            if self.turn == -1:
                sender.image = self.p1
                sound.play_effect('digital:Laser7')
                self.take_turn()
            elif self.turn == 1:
                sender.image = self.p2
                sound.play_effect('digital:SpaceTrash1')
                self.take_turn()
            self.check_status()

    def board_setup(self):
        # Set initial view alpha's and board layout
        l3.alpha = 0
        b10.alpha = 0
        self.p1 = ui.Image.named('Astronaut1.JPG').with_rendering_mode(
            ui.RENDERING_MODE_ORIGINAL)
        self.p2 = ui.Image.named('Alien1.JPG').with_rendering_mode(
            ui.RENDERING_MODE_ORIGINAL)
        self.start_image = ui.Image.named(
            'emj:Blue_Circle').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
        self.button_list = (b1, b2, b3, b4, b5, b6, b7, b8, b9)
        for btn in self.button_list:
            btn.image = self.start_image

    def check_status(self):
        # Checks posible wins against board
        self.board_now = ({
            1: b1.image,
            2: b2.image,
            3: b3.image,
        }, {
            4: b4.image,
            5: b5.image,
            6: b6.image,
        }, {
            7: b7.image,
            8: b8.image,
            9: b9.image,
        }, {
            1: b1.image,
            4: b4.image,
            7: b7.image
        }, {
            2: b2.image,
            5: b5.image,
            8: b8.image
        }, {
            3: b3.image,
            6: b6.image,
            9: b9.image
        }, {
            1: b1.image,
            5: b5.image,
            9: b9.image
        }, {
            3: b3.image,
            5: b5.image,
            7: b7.image
        }, )
        wins = ({
            1: self.p1,
            2: self.p1,
            3: self.p1
        }, {
            4: self.p1,
            5: self.p1,
            6: self.p1
        }, {
            7: self.p1,
            8: self.p1,
            9: self.p1
        }, {
            1: self.p1,
            4: self.p1,
            7: self.p1
        }, {
            2: self.p1,
            5: self.p1,
            8: self.p1
        }, {
            3: self.p1,
            6: self.p1,
            9: self.p1
        }, {
            1: self.p1,
            5: self.p1,
            9: self.p1
        }, {
            3: self.p1,
            5: self.p1,
            7: self.p1
        }, {
            1: self.p2,
            2: self.p2,
            3: self.p2
        }, {
            4: self.p2,
            5: self.p2,
            6: self.p2
        }, {
            7: self.p2,
            8: self.p2,
            9: self.p2
        }, {
            1: self.p2,
            4: self.p2,
            7: self.p2
        }, {
            2: self.p2,
            5: self.p2,
            8: self.p2
        }, {
            3: self.p2,
            6: self.p2,
            9: self.p2
        }, {
            1: self.p2,
            5: self.p2,
            9: self.p2
        }, {
            3: self.p2,
            5: self.p2,
            7: self.p2
        }, )
        for win in wins:
            if win in self.board_now:
                l1.alpha = 0
                l2.alpha = 0
                l3.alpha = 1
                l4.alpha = 0
                b10.alpha = 1
                b10.image = list(win.values())[1]
                sound.play_effect('voice:male_you_win')
                for btn in self.button_list:
                    btn.alpha = 0
        current_image = []
        for btn in self.button_list:
            current_image.append(btn.image)
        for btn in self.button_list:
            if self.start_image not in current_image:
                l1.alpha = 0
                l2.alpha = 0
                l3.alpha = 0
                l4.alpha = 1
                b10.alpha = 1
                for btn in self.button_list:
                    btn.alpha = 0
                b10.image = ui.Image.named('Tie.PNG').with_rendering_mode(
            ui.RENDERING_MODE_ORIGINAL)
                sound.play_effect('voice:male_its_a_tie')


v = TTTView()
view = ui.load_view('tic-tac-toe.pyui')
b1 = view['button1']
b2 = view['button2']
b3 = view['button3']
b4 = view['button4']
b5 = view['button5']
b6 = view['button6']
b7 = view['button7']
b8 = view['button8']
b9 = view['button9']
b10 = view['button10']
l1 = view['label1']
l2 = view['label2']
l3 = view['label3']
l4 = view['label4']
v.board_setup()
v.check_status()
view.present("fullscreen")
