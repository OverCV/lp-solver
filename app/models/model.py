from pulp import *
from math import *


def logger(func: callable) -> callable:
    ''' Function to log the model. '''

    def wrapper(self) -> None:
        print(f'\n{func(self)}\n')
    return wrapper


class Model:
    ''' Class Model is used to solve problems. '''

    def __init__(
        self, maximizable: bool, num_variables: int
    ) -> object:
        self._maximizar: bool = maximizable
        self._variables: int = num_variables
        self._problema: LpProblem = None

    def limitar(self, funcion_z: str, *restricciones: str) -> object:
        ''' Function to set the data of the model. '''
        objetivo: int = int(cos(self._maximizar * pi))

        self._problema: LpProblem = LpProblem(
            'Problema optimización', objetivo
        )

        x = [LpVariable(f'X{i}', lowBound=0) for i in range(self._variables+1)]

        for rest in restricciones:
            self._problema += eval(rest)

        self._problema += eval(funcion_z)

    @logger
    def resolver(self) -> str:
        ''' Function to solve the model. '''
        _out_vars = 'Se ha llegado a un óptimo.\nTal que'

        try:
            self._problema.solve()

            if LpStatus[self._problema.status] == 'Optimal':
                for _var in self._problema.variables():
                    _out_vars += f', {_var.name} = {_var.varValue}'
                return f'{_out_vars}.\nCon z = {self._problema.objective.value()}.'

            else:
                return f'El problema no tiene solución óptima. Estado: {LpStatus[self._problema.status]}'

        except Exception as e:
            return f'Error al resolver el problema: {str(e)}'
