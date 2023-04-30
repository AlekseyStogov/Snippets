from django import template
register = template.Library()


def is_empty(value, alt):
   if value:
       return value
   return alt


register.filter('is_empty', is_empty)

#пример вызова шаблонного фильтра
# {{"text"| is_empty: "other"}}
# "text"---->value
# "other" ----> alt
# return alt ----> "is_empty"
# не забываем подгрузить через ЛОАД МАЙ ТАГС