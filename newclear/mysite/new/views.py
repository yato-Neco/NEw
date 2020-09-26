from django.shortcuts import render
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse


x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
y = [3, 5, 0, 5, 6, 10, 2]
def setPlt(x,y):
    
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Test}$", color='#3407ba')
    plt.xlabel("x")
    plt.ylabel("y")

def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def test_print(request):
    setPlt(x,y)
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
# Create your views here.
