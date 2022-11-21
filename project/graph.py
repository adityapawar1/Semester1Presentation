from manim import Axes, Scene


class TwoDIntro(Scene):
    @staticmethod
    def fx(x: float):
        return x**2

    def construct(self):
        axes = Axes([0, 10, 1], [0, 10, 1], 10, 10)
        axes.add_coordinates()
