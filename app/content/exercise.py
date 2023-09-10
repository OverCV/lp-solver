from models.model import Model
# import os
# from contextlib import redirect_stdout


class Exercise:
    ''' Class Exercises is used to practics linear programming. '''

    def __init__(self) -> None:
        pass

    def EX1(self) -> str:
        ''' Exercise 01. '''
        _model = Model(True, 2)
        _model.limitar(
            '2000*x[1] + 3000*x[2]',
            'x[1] + x[2] <= 4',
            '2*x[1] + x[2] <= 10',
            '400*x[1] + 200*x[2] <= 1200',
        )
        _model.resolver()

    def EX2(self) -> str:
        ''' Exercise 02. '''
        _model = Model(True, 2)
        _model.limitar(
            '1200*x[1] + 1400*x[2]',
            'x[1] + 2*x[2]<= 800',
            '2*x[1] + x[2]<= 800',
            'x[1] + x[2]<= 500',

        )
        _model.resolver()

    def EX4(self) -> str:
        ''' Exercise 04. '''
        _model = Model(False, 2)
        _model.limitar(
            '150*x[1] + 300*x[2]',
            '8*x[1] + 2*x[2] >= 16',
            'x[1] + x[2] >= 5',
            '2*x[1] + 7*x[2] >= 20',
        )
        _model.resolver()

    def EX5(self) -> str:
        ''' Exercise 05. '''
        _model = Model(False, 2)
        _model.limitar(
            '150*x[1] + 750*x[2]',
            'x[1] + x[2] >= 70',
            '2*x[1] + 2*x[2] >= 130',
            '4*x[1] + 2*x[2] >= 150',
        )
        _model.resolver()
