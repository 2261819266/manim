from manimlib import *

class DRAW(Scene):
    def construct(self) -> None:
        cir1 = Circle()
        cir2 = Circle()

        self.add(cir1, cir2)
        cir2.move_to(UP * 2, coor_mask=np.array([1, 0, 1]))

        self.wait()