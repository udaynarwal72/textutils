"""I made this file : Uday Singh"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyzed(request):
    # Getting input from user
    user_text = request.GET.get('text', 'default')
    user_input_removepunc = request.GET.get('removepunc_checkbox', 'of')
    user_input_fullcaps = request.GET.get('fullcaps_checkbox', 'of')
    user_input_removeline = request.GET.get('removeline_checkbox', 'of')
    user_input_removeextraspace = request.GET.get(
        'removeextraspace_checkbox', 'of')
    user_input_charactercount = request.GET.get(
        'charactercount_checkbox', 'of')

    # Backend coding
    if user_input_removepunc == "on":
        punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        user_text_result = ""
        for char in user_text:
            if char not in punctuations:
                user_text_result = user_text_result + char
        params = {"purpose": "Remove Punctuations",
                  "text_analyzed": user_text_result}
        return render(request, 'analyze.html', params)
    elif user_input_fullcaps == "on":
        user_text_result = ""
        for char in user_text:
            user_text_result = user_text_result + char.upper()
        params = {"purpose": "capitalize", "text_analyzed": user_text_result}
        return render(request, 'analyze.html', params)
    elif user_input_removeline == "on":
        user_text_result = ""
        for char in user_text:
            if char != "\n":
                user_text_result = user_text_result + char
        params = {"purpose": "remove Line", "text_analyzed": user_text_result}
        return render(request, 'analyze.html', params)
    elif user_input_removeextraspace == "on":
        user_text_result = user_text.replace("  ", " ")
        params = {"purpose": "remove Line", "text_analyzed": user_text_result}
        return render(request, 'analyze.html', params)
    elif user_input_charactercount == "on":
        user_text_result = f"Your character count is {len(user_text)}"
        params = {"purpose": "remove Line", "text_analyzed": user_text_result}
        return render(request, 'analyze.html', params)
    else:
        params = {"purpose": "Error" , "text_analyzed" :"Please use any function"}
        return render(request, 'analyze.html', params)
