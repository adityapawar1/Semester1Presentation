from manim import *

class SA_Practice_Problem_1(ThreeDScene):
    @staticmethod
    def fx(x: float):
        return 16 - x ** 2
    
    def construct(self):
        self.begin_ambient_camera_rotation()
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[0, 4.1, 1],
            x_length=5,
            y_range=[0, 16.1, 4],
            y_length=5,
            z_range=[-16.1, 16.1, 4],
            z_length=5,
        ).add_coordinates().move_to(LEFT)

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
        ).move_to(LEFT)

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

        self.wait()

        problem = MathTex("Find \ SA: \ y=16-x^2, 0\leq x\leq 4").move_to(UR)
        solve1 = MathTex("S = 2\pi\int_{0}^{4}x\sqrt{1+4x^2}dx")
        solve2 = MathTex("let \ u = 1+4x^2, \ du=8xdx,\ x=0:u=1, x=4:u=65")
        solve3 = MathTex("\frac{2 \pi}{8}\int_{1}^{65}u^{1/2}du")
        solve4 = MathTex("\frac{\pi}{4}\cdot \frac{2}{3}u^{\frac{3}{2}}\Biggr|_{1}^{9}")
        answer = MathTex("\frac{\pi}{6}(65^{\frac{3}{2}}-1) \ units^{2}")
        box = SurroundingRectangle(answer, buff=0.1)

        self.play(Write(problem))
        self.wait()
        self.play(Write(solve1))
        self.wait()
        self.play(Write(solve2))
        self.wait()
        self.play(Write(solve3))
        self.wait()
        self.play(Write(solve4))
        self.wait()
        self.play(Write(answer))
        self.wait()
        self.play(Create(box), run_time=5)





