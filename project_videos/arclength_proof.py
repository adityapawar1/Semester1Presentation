from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    PI,
    PURPLE,
    RIGHT,
    UL,
    UP,
    UR,
    Axes,
    Brace,
    Create,
    DrawBorderThenFill,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    NumberPlane,
    ReplacementTransform,
    Scene,
    Text,
    TransformMatchingTex,
    VGroup,
    ValueTracker,
    Write,
    RED,
    color_gradient,
)
import numpy as np


class ArcLengthVisualizationScene(Scene):
    x_range = [-5, 5, 1]

    @staticmethod
    def fx(x: float):
        return np.sin(x) + 2 * np.cos(20 / 11 * x) + 4
        # return -(x**2) + 5

    def construct(self):
        plane = Axes(x_range=self.x_range, y_range=[-2, 9], x_length=10, y_length=10)
        self.draw_graph(plane)
        self.arc_length_visualization(plane)

    def draw_graph(self, plane):
        axes_label = plane.get_axis_labels("x", "f(x)")

        graph = plane.plot(self.fx, color=PURPLE)

        self.play(DrawBorderThenFill(plane), Write(axes_label))
        self.play(Create(graph), run_time=2)
        self.wait()

    def arc_length_visualization(self, plane):
        # distance_label = MathTex(r"d=\sqrt{x^2+y^2}").next_to(arc_line, LEFT, buff=0.2)
        number_of_lines_label = (
            Text("Number of lines: ").move_to(UR).shift(RIGHT * 3).shift(UP * 2)
        )
        number_of_lines_counter = Text("1").next_to(
            number_of_lines_label, RIGHT, buff=0.2
        )

        min = self.x_range[0]
        max = self.x_range[1]
        past_lines = VGroup()

        def create_arc_length_part(plane, x0, x1):
            point0 = plane.c2p(x0, self.fx(x0))
            point1 = plane.c2p(x1, self.fx(x1))

            return Line(point0, point1, color=RED)

        for i in range(7):
            num_lines = 2**i
            step = (max - min) / num_lines

            current_lines = VGroup(
                *[
                    create_arc_length_part(
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
        infinity_counter = MathTex(r"\infty").next_to(
            number_of_lines_label, RIGHT, buff=0.1
        )
        update_label_animation = ReplacementTransform(
            number_of_lines_counter, infinity_counter
        )
        self.play(
            FadeIn(limit_of_arc_length), FadeOut(past_lines), update_label_animation
        )


class ArcLengthProofScene(Scene):
    x_range = [-5, 5, 1]

    @staticmethod
    def fx(x: float):
        return np.sin(x * 1 / 4 + 0.1) + 2 * np.cos(15 / 11 * x) + 4

    def construct(self):
        plane = (
            Axes(
                x_range=self.x_range,
                y_range=[-2, 9],
                x_length=7,
                y_length=7,
            )
            .move_to(RIGHT)
            .shift(RIGHT * 1.2)
        )
        self.draw_graph(plane)

    def draw_graph(self, plane):
        axes_label = plane.get_axis_labels("x", "f(x)")

        graph = plane.plot(self.fx, color=PURPLE).set_color_by_gradient(GREEN, BLUE)

        self.play(DrawBorderThenFill(plane), Write(axes_label))
        self.play(Create(graph), run_time=2)
        self.wait()

        x0, x1 = -5, 5
        point0 = plane.c2p(x0, self.fx(x0))
        point1 = plane.c2p(x1, self.fx(x1))

        line = Line(point0, point1, color=RED)
        line_brace = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())

        x_label = MathTex(r"\Delta x")
        y_label = MathTex(r"\Delta y")

        x_brace = Brace(line).put_at_tip(x_label)
        y_brace = Brace(line, direction=[1, 0, 0]).put_at_tip(y_label)

        self.play(FadeIn(line))
        self.play(FadeIn(line_brace))
        self.play(FadeIn(x_brace, x_label))
        self.play(FadeIn(y_brace, y_label))

        distance_formula = (
            MathTex(r"s=\sqrt{(\Delta x)^2+(\Delta y)^2}")
            .move_to(UL)
            .shift(UL * 2)
            .shift(LEFT)
        )
        summation = MathTex(
            r"=\sum_{i=1}^{n} \sqrt{(\Delta x)^2+(\Delta y)^2}"
        ).next_to(distance_formula, DOWN, buff=0.2)

        self.play(FadeIn(distance_formula))
        self.play(ReplacementTransform(distance_formula.copy(), summation))
        self.play(FadeOut(line, line_brace))
        self.play(FadeOut(x_brace, x_label))
        self.play(FadeOut(y_brace, y_label))

        number_of_lines_label = MathTex("n=").move_to(UP).shift(UP * 1.0)
        number_of_lines_counter = MathTex("1").next_to(
            number_of_lines_label, RIGHT, buff=0.2
        )
        summation_replacement = (
            MathTex(r"=\sum_{i=1}^{n}")
            .next_to(distance_formula, DOWN, buff=0.2)
            .shift(LEFT * 0.4)
        )
        self.play(
            ReplacementTransform(
                summation_replacement,
                VGroup(number_of_lines_label, number_of_lines_counter),
                run_time=2,
            )
        )

        min = self.x_range[0]
        max = self.x_range[1]
        past_lines = VGroup()

        def create_arc_length_part(plane, x0, x1):
            point0 = plane.c2p(x0, self.fx(x0))
            point1 = plane.c2p(x1, self.fx(x1))

            return Line(point0, point1, color=RED)

        for i in range(7):
            num_lines = 2**i
            step = (max - min) / num_lines

            current_lines = VGroup(
                *[
                    create_arc_length_part(
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
            updated_NOL_counter = MathTex(str(num_lines)).next_to(
                number_of_lines_label, RIGHT, buff=0.2
            )
            update_label_animation = ReplacementTransform(
                number_of_lines_counter, updated_NOL_counter
            )

            self.play(line_animation, update_label_animation)
            self.wait()

            past_lines = current_lines
            number_of_lines_counter = updated_NOL_counter

        infinity_counter = MathTex(r"\infty").next_to(
            number_of_lines_label, RIGHT, buff=0.1
        )
        self.play(ReplacementTransform(number_of_lines_counter, infinity_counter))

        # summation_step_2 = MathTex(
        #     r"=\sum_{i=1}^{n} \sqrt{\Delta x^2+\Delta y^2 \frac{\Delta x^2}{\Delta x^2}}"
        # ).next_to(distance_formula, DOWN, buff=0.2)
        summation_step_2 = MathTex(
            r"=\sum_{i=1}^{n}",
            r"\sqrt{\Delta x^2 + \Delta x^2 \frac{\Delta y^2}{\Delta x^2}}",
        ).next_to(distance_formula, DOWN, buff=0.2)

        self.play(
            ReplacementTransform(summation, summation_step_2), FadeOut(infinity_counter)
        )

        summation_step_2 = MathTex(
            r"=\sum_{i=1}^{n}",
            r"\sqrt{\Delta x^2 + \Delta x^2 \frac{\Delta y^2}{\Delta x^2}}",
        ).next_to(distance_formula, DOWN, buff=0.2)

        # self.play(Write(summation_step_3), FadeOut(infinity_counter))
