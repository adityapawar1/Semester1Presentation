from manim import *

class SA_Practice_Problem_1(ThreeDScene):
    @staticmethod
    def fx(x: float):
        return 0.25 * x ** 2
    
    def construct(self):
        self.begin_ambient_camera_rotation()
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[0, 4.1, 1],
            x_length=5,
            y_range=[-4, 4.1, 1],
            y_length=5,
            z_range=[-4, 4, 1],
            z_length=5,
        ).add_coordinates()

        function = axes.plot(self.fx, x_range=[0, 4], color=YELLOW)
        area = axes.get_area(graph=function, x_range=[0, 4], color=[BLUE_B, BLUE_D])

        e = ValueTracker(2 * PI)
        surface = always_redraw(
            lambda: Surface(
                lambda u, v: axes.c2p(
                    v, self.fx(v) * np.cos(u), self.fx(v) * np.sin(u)
                ),
                u_range=[0, e.get_value()],
                v_range=[0, 4],
                checkerboard_colors=[BLUE_B, BLUE_D],
            )
        )

        self.play(
            LaggedStart(Create(axes), Create(function), Create(area), Create(surface)),
            run_time=4,
            lag_ratio=0.5,
        )

        self.play(
            Rotating(
                VGroup(function, area),
                axis=RIGHT,
                radians=2 * PI,
                about_point=axes.c2p(0, 0, 0),
            ),
            e.animate.set_value(2 * PI),
            run_time=5,
            rate_func=linear,
        )