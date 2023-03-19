from fastapi.routing import APIRoute


def controller_and_function_name(route: APIRoute) -> str:
    """
    Generate an `operation_id` of an endpoint based on its controller and function name.

    Assumes the route has a `/api` prefix in its path.
    """
    controller_name = _extract_controller_name(route)
    return f"{controller_name}_{route.name}"


def _extract_controller_name(route: APIRoute) -> str:
    """
    Assumes the input route has a `/api` prefix in its path.
    """
    try:
        return route.path.split("/")[2]
    except IndexError as index_error:
        raise ValueError(
            f'A caminho do endpoint "{route.path}" é inválido. Uma rota deve ser composta pelo prefixo "/api" '
            f"seguido pelo nome do recurso do controller. Exemplo: /api/resource/. Certifique-se de que o nome "
            f"do recurso do controller está especificado como prefix do respectivo router."
        ) from index_error
