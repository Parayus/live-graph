
import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as pp
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.animation as animation
import mpl_finance
from mpl_finance import candlestick_ohlc
from matplotlib import style
from IPython.display import HTML
import seaborn




get_ipython().run_line_magic('matplotlib', 'notebook')


style.use(['seaborn'])
fig = pp.figure(1,figsize=(7,4))
ax1 = fig.add_subplot(1,1,1)
pp.title('data')
def animate(i):
    data=[]
    data2=[]
    try:
        conn = sqlite3.connect("testDB.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM weights")
 
        rows = cur.fetchall()
 
    except Error as e:
        print(e)
    
    ax1.clear()
    ax1.plot(rows)
    
ani = animation.FuncAnimation(fig,animate,interval = 1000)





