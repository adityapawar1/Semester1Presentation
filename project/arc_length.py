from manim import (
    BLUE,
    DOWN,
    DR,
    LEFT,
    PURPLE,
    RIGHT,
    UP,
    UR,
    Axes,
    Create,
    Dot,
    DrawBorderThenFill,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    NumberPlane,
    ReplacementTransform,
    Scene,
    Text,
    VGroup,
    Write,
    RED,
    always_redraw,
    color,
)
import numpy as np


class ArcLengthProofScene(Scene):
    x_range = [-5, 5, 1]

    @staticmethod
    def fx(x: float):
        return np.sin(x) + 2 * np.cos(20 / 11 * x) + 4
        # return -(x**2) + 5

    def construct(self):
        plane = Axes(x_range=self.x_range, y_range=[-2, 9], x_length=10, y_length=10)

        # plane.add_coordinates()

        axes_label = plane.get_axis_labels("x", "f(x)")

        graph = plane.plot(self.fx, color=PURPLE)

        self.play(DrawBorderThenFill(plane), Write(axes_label))
        self.play(Create(graph), run_time=2)
        self.wait()

        # distance_label = MathTex(r"d=\sqrt{x^2+y^2}").next_to(arc_line, LEFT, buff=0.2)
        number_of_lines_label = (
            Text("Number of lines: ").move_to(UR).shift(RIGHT * 3).shift(UP * 2)
        )
        number_of_lines_counter = Text("1").next_to(
            number_of_lines_label, RIGHT, buff=0.2
        )
        self.play(Write(number_of_lines_label), Write(number_of_lines_counter))

        min = self.x_range[0]
        max = self.x_range[1]
        past_lines = VGroup()

        for i in range(7):
            num_lines = 2**i
            step = (max - min) / num_lines

            current_lines = VGroup(
                *[
                    self.create_arc_length_part(
                        plane, min + step * (j), min + step * (j + 1)
                    )
                    for j in range(num_lines)
                ]
            )

            line_animation = (
                FadeIn(current_lines)
                if i == 0
                else ReplacementTransform(past_lines, current_lines)
            )
            updated_NOL_counter = Text(str(num_lines)).next_to(
                number_of_lines_label, RIGHT, buff=0.1
            )
            update_label_animation = ReplacementTransform(
                number_of_lines_counter, updated_NOL_counter
            )

            self.play(line_animation, update_label_animation)
            self.wait()

            past_lines = current_lines
            number_of_lines_counter = updated_NOL_counter

        limit_of_arc_length = plane.plot(self.fx, color=RED)
        self.play(FadeIn(limit_of_arc_length), FadeOut(past_lines))

        # self.play(FadeIn(dot1, dot2))
        # self.play(FadeIn(arc_line))
        # self.play(Write(distance_label))

    def create_arc_length_part(self, plane, x0, x1):
        point0 = plane.c2p(x0, self.fx(x0))
        point1 = plane.c2p(x1, self.fx(x1))

        # dot1 = Dot(point0, color=RED)
        # dot2 = Dot(point1, color=RED)
        arc_line = Line(point0, point1, color=RED)

        return arc_line
