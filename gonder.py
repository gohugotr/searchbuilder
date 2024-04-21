#  Author:      Cengiz YILMAZ
#  Info:        http://datatables.net


def filter_string_fields(
    q_objects, field_name, field_type, condition, field_value, field_value2, logic_value
):

    if field_name and field_type:
        if field_type == "string" or field_type == "select":
            if condition == "contains":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__icontains": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__icontains": field_value})
            elif condition == "starts":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__istartswith": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__istartswith": field_value})
            elif condition == "=":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__iexact": field_value})
            elif condition == "ends":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__iendswith": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__iendswith": field_value})
            elif condition == "null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
            elif condition == "!starts":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__istartswith": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__istartswith": field_value})
            elif condition == "!contains":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__icontains": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__icontains": field_value})
            elif condition == "!=":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__iexact": field_value})
            elif condition == "!ends":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__iendswith": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__iendswith": field_value})
            elif condition == "!null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
        elif field_type == "date":
            if condition == "<":
                q_objects &= Q(**{field_name + "__lt": field_value})
            elif condition == ">":
                q_objects &= Q(**{field_name + "__gt": field_value})
            elif condition == "between":
                q_objects &= Q(
                    **{
                        field_name
                        + "__range": (field_value, field_value2 or date.today())
                    }
                )
            elif condition == "!between":
                q_objects &= ~Q(
                    **{
                        field_name
                        + "__range": (field_value, field_value2 or date.today())
                    }
                )
            elif condition == "null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
            elif condition == "=":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__iexact": field_value})
            elif condition == "!=":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__iexact": field_value})
            elif condition == "!null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
        elif field_type == "num":
            if condition == "between":
                q_objects &= Q(**{field_name + "__range": (field_value, field_value2)})
            elif condition == "null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
            elif condition == "=":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__iexact": field_value})
            elif condition == ">":
                q_objects &= Q(**{field_name + "__gt": field_value})
            elif condition == ">=":
                q_objects &= Q(**{field_name + "__gte": field_value})
            elif condition == "<":
                q_objects &= Q(**{field_name + "__lt": field_value})
            elif condition == "<=":
                q_objects &= Q(**{field_name + "__lte": field_value})
            elif condition == "!between":
                q_objects &= ~Q(**{field_name + "__range": (field_value, field_value2)})
            elif condition == "!=":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__iexact": field_value})
            elif condition == "!null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
        elif field_type == "array":
            if condition == "contains":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__icontains": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__icontains": field_value})
            elif condition == "=":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__iexact": field_value})
            elif condition == "null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": True}) | Q(
                        **{field_name: ""}
                    )
            elif condition == "without":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__icontains": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__icontains": field_value})
            elif condition == "!=":
                if logic_value == "AND":
                    q_objects &= ~Q(**{field_name + "__iexact": field_value})
                elif logic_value == "OR":
                    q_objects |= ~Q(**{field_name + "__iexact": field_value})
            elif condition == "!null":
                if logic_value == "AND":
                    q_objects &= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
                elif logic_value == "OR":
                    q_objects |= Q(**{field_name + "__isnull": False}) & ~Q(
                        **{field_name: ""}
                    )
    return q_objects
