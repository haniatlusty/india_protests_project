{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3c71165c-8942-4a4f-98f4-0502fd38e1ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "using StatsKit, Query, Dates, VegaLite;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c29e7d3a-3d57-497e-be46-179fc0ec9528",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = CSV.read(\"../data/2016-2022.csv\", DataFrame);"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e4e86e2-8ba0-40e7-9c81-1f0be512b015",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "528ad4e9-d5cf-4677-b8e8-019172552f70",
   "metadata": {},
   "source": [
    "## Segregowanie danych"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7b68cb3-67c9-4110-9418-3b977327cb1c",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1b4ee940-6ef2-4248-858c-18e0bff12d7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "function year_data(data, year, location)\n",
    "    df_2016 = @from i in data begin\n",
    "        @where i.year == year\n",
    "        @where i.location == location\n",
    "        @select {i.event_date, i.event_type, i.sub_event_type}\n",
    "        @collect DataFrame\n",
    "    end\n",
    "end;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "da2e9ea0-36d9-45fa-aa94-4b257924b989",
   "metadata": {},
   "outputs": [],
   "source": [
    "function plot_year_city(data, year, location, sub=false)\n",
    "    dt = year_data(data, year, location)                                                # wczytanie danych dla danego miasta i danego roku\n",
    "    dates = Dates.value.(Date.(dt.event_date, dateformat\"d U y\").-Date(year,1,1))       # przekształcenie dat na dni konkretnego roku\n",
    "    select!(dt, Not(:event_date)); insertcols!(dt, 1, :time => dates);                  # podmienie kolumny dat w df\n",
    "    sort!(dt)                                                                           # sortowanie df\n",
    "    n = [length(sub ? d.sub_event_type : d.event_type) for d in groupby(dt, :time)];    # ilość wydarzeń danego dnia\n",
    "    t = unique(dt.time);                                                                # odpowiadająca lista dni (w kolejności)\n",
    "    plot = @vlplot(\n",
    "        height=600,\n",
    "        width=1200,\n",
    "        :bar,\n",
    "        x=t,\n",
    "        y=n,\n",
    "        title = location*\" in \"*string(year)\n",
    "    )\n",
    "    return ((t, n), plot, isleapyear(year))\n",
    "end;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "404f99c1-e7df-4c02-8876-67e2511f3181",
   "metadata": {},
   "outputs": [],
   "source": [
    "dat, plot, leap = plot_year_city(df, 2018, \"Imphal\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "919f3188-ee88-4302-9515-168202b5091a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.vegalite.v4+json": {
       "data": {
        "values": [
         {
          "x": 8,
          "y": 1
         },
         {
          "x": 10,
          "y": 1
         },
         {
          "x": 14,
          "y": 1
         },
         {
          "x": 15,
          "y": 2
         },
         {
          "x": 16,
          "y": 1
         },
         {
          "x": 18,
          "y": 1
         },
         {
          "x": 20,
          "y": 2
         },
         {
          "x": 22,
          "y": 1
         },
         {
          "x": 26,
          "y": 2
         },
         {
          "x": 27,
          "y": 2
         },
         {
          "x": 29,
          "y": 1
         },
         {
          "x": 30,
          "y": 2
         },
         {
          "x": 31,
          "y": 1
         },
         {
          "x": 35,
          "y": 3
         },
         {
          "x": 36,
          "y": 3
         },
         {
          "x": 37,
          "y": 1
         },
         {
          "x": 57,
          "y": 1
         },
         {
          "x": 58,
          "y": 1
         },
         {
          "x": 64,
          "y": 2
         },
         {
          "x": 65,
          "y": 1
         },
         {
          "x": 66,
          "y": 2
         },
         {
          "x": 70,
          "y": 2
         },
         {
          "x": 72,
          "y": 1
         },
         {
          "x": 78,
          "y": 1
         },
         {
          "x": 80,
          "y": 1
         },
         {
          "x": 81,
          "y": 1
         },
         {
          "x": 91,
          "y": 1
         },
         {
          "x": 94,
          "y": 1
         },
         {
          "x": 96,
          "y": 1
         },
         {
          "x": 97,
          "y": 2
         },
         {
          "x": 98,
          "y": 2
         },
         {
          "x": 99,
          "y": 2
         },
         {
          "x": 101,
          "y": 2
         },
         {
          "x": 102,
          "y": 3
         },
         {
          "x": 104,
          "y": 1
         },
         {
          "x": 105,
          "y": 2
         },
         {
          "x": 106,
          "y": 1
         },
         {
          "x": 108,
          "y": 1
         },
         {
          "x": 109,
          "y": 1
         },
         {
          "x": 110,
          "y": 2
         },
         {
          "x": 112,
          "y": 1
         },
         {
          "x": 113,
          "y": 2
         },
         {
          "x": 114,
          "y": 1
         },
         {
          "x": 115,
          "y": 2
         },
         {
          "x": 116,
          "y": 2
         },
         {
          "x": 117,
          "y": 1
         },
         {
          "x": 119,
          "y": 2
         },
         {
          "x": 121,
          "y": 3
         },
         {
          "x": 123,
          "y": 1
         },
         {
          "x": 124,
          "y": 1
         },
         {
          "x": 126,
          "y": 2
         },
         {
          "x": 127,
          "y": 1
         },
         {
          "x": 128,
          "y": 4
         },
         {
          "x": 129,
          "y": 3
         },
         {
          "x": 130,
          "y": 1
         },
         {
          "x": 131,
          "y": 1
         },
         {
          "x": 132,
          "y": 1
         },
         {
          "x": 133,
          "y": 2
         },
         {
          "x": 134,
          "y": 1
         },
         {
          "x": 136,
          "y": 2
         },
         {
          "x": 140,
          "y": 2
         },
         {
          "x": 141,
          "y": 1
         },
         {
          "x": 142,
          "y": 2
         },
         {
          "x": 144,
          "y": 1
         },
         {
          "x": 145,
          "y": 2
         },
         {
          "x": 149,
          "y": 2
         },
         {
          "x": 154,
          "y": 2
         },
         {
          "x": 155,
          "y": 2
         },
         {
          "x": 156,
          "y": 4
         },
         {
          "x": 158,
          "y": 1
         },
         {
          "x": 159,
          "y": 1
         },
         {
          "x": 160,
          "y": 2
         },
         {
          "x": 161,
          "y": 1
         },
         {
          "x": 162,
          "y": 1
         },
         {
          "x": 170,
          "y": 1
         },
         {
          "x": 171,
          "y": 1
         },
         {
          "x": 172,
          "y": 1
         },
         {
          "x": 173,
          "y": 2
         },
         {
          "x": 176,
          "y": 1
         },
         {
          "x": 179,
          "y": 1
         },
         {
          "x": 180,
          "y": 1
         },
         {
          "x": 181,
          "y": 1
         },
         {
          "x": 182,
          "y": 2
         },
         {
          "x": 184,
          "y": 3
         },
         {
          "x": 185,
          "y": 2
         },
         {
          "x": 186,
          "y": 1
         },
         {
          "x": 187,
          "y": 3
         },
         {
          "x": 188,
          "y": 1
         },
         {
          "x": 189,
          "y": 3
         },
         {
          "x": 191,
          "y": 1
         },
         {
          "x": 193,
          "y": 1
         },
         {
          "x": 194,
          "y": 1
         },
         {
          "x": 195,
          "y": 1
         },
         {
          "x": 196,
          "y": 3
         },
         {
          "x": 197,
          "y": 6
         },
         {
          "x": 198,
          "y": 2
         },
         {
          "x": 199,
          "y": 1
         },
         {
          "x": 200,
          "y": 1
         },
         {
          "x": 201,
          "y": 2
         },
         {
          "x": 203,
          "y": 3
         },
         {
          "x": 204,
          "y": 1
         },
         {
          "x": 207,
          "y": 2
         },
         {
          "x": 208,
          "y": 5
         },
         {
          "x": 209,
          "y": 2
         },
         {
          "x": 210,
          "y": 3
         },
         {
          "x": 211,
          "y": 3
         },
         {
          "x": 212,
          "y": 2
         },
         {
          "x": 213,
          "y": 1
         },
         {
          "x": 214,
          "y": 3
         },
         {
          "x": 215,
          "y": 1
         },
         {
          "x": 216,
          "y": 1
         },
         {
          "x": 217,
          "y": 2
         },
         {
          "x": 218,
          "y": 2
         },
         {
          "x": 219,
          "y": 3
         },
         {
          "x": 220,
          "y": 6
         },
         {
          "x": 221,
          "y": 2
         },
         {
          "x": 222,
          "y": 4
         },
         {
          "x": 223,
          "y": 1
         },
         {
          "x": 225,
          "y": 1
         },
         {
          "x": 227,
          "y": 1
         },
         {
          "x": 230,
          "y": 2
         },
         {
          "x": 232,
          "y": 7
         },
         {
          "x": 234,
          "y": 3
         },
         {
          "x": 235,
          "y": 3
         },
         {
          "x": 236,
          "y": 1
         },
         {
          "x": 237,
          "y": 3
         },
         {
          "x": 238,
          "y": 1
         },
         {
          "x": 241,
          "y": 2
         },
         {
          "x": 244,
          "y": 1
         },
         {
          "x": 245,
          "y": 1
         },
         {
          "x": 248,
          "y": 1
         },
         {
          "x": 249,
          "y": 2
         },
         {
          "x": 250,
          "y": 3
         },
         {
          "x": 252,
          "y": 1
         },
         {
          "x": 254,
          "y": 1
         },
         {
          "x": 259,
          "y": 1
         },
         {
          "x": 260,
          "y": 1
         },
         {
          "x": 262,
          "y": 2
         },
         {
          "x": 263,
          "y": 1
         },
         {
          "x": 266,
          "y": 4
         },
         {
          "x": 268,
          "y": 1
         },
         {
          "x": 269,
          "y": 2
         },
         {
          "x": 270,
          "y": 1
         },
         {
          "x": 271,
          "y": 1
         },
         {
          "x": 275,
          "y": 1
         },
         {
          "x": 276,
          "y": 1
         },
         {
          "x": 278,
          "y": 1
         },
         {
          "x": 279,
          "y": 1
         },
         {
          "x": 282,
          "y": 2
         },
         {
          "x": 291,
          "y": 1
         },
         {
          "x": 292,
          "y": 1
         },
         {
          "x": 296,
          "y": 1
         },
         {
          "x": 300,
          "y": 1
         },
         {
          "x": 303,
          "y": 1
         },
         {
          "x": 305,
          "y": 1
         },
         {
          "x": 306,
          "y": 1
         },
         {
          "x": 307,
          "y": 1
         },
         {
          "x": 310,
          "y": 1
         },
         {
          "x": 311,
          "y": 1
         },
         {
          "x": 314,
          "y": 1
         },
         {
          "x": 316,
          "y": 1
         },
         {
          "x": 319,
          "y": 1
         },
         {
          "x": 320,
          "y": 2
         },
         {
          "x": 331,
          "y": 1
         },
         {
          "x": 333,
          "y": 2
         },
         {
          "x": 335,
          "y": 1
         },
         {
          "x": 336,
          "y": 1
         },
         {
          "x": 337,
          "y": 1
         },
         {
          "x": 339,
          "y": 2
         },
         {
          "x": 341,
          "y": 2
         },
         {
          "x": 342,
          "y": 1
         },
         {
          "x": 345,
          "y": 2
         },
         {
          "x": 346,
          "y": 2
         },
         {
          "x": 348,
          "y": 1
         },
         {
          "x": 350,
          "y": 1
         },
         {
          "x": 354,
          "y": 1
         },
         {
          "x": 355,
          "y": 1
         },
         {
          "x": 356,
          "y": 1
         },
         {
          "x": 357,
          "y": 1
         },
         {
          "x": 359,
          "y": 1
         },
         {
          "x": 360,
          "y": 2
         },
         {
          "x": 362,
          "y": 2
         }
        ]
       },
       "encoding": {
        "x": {
         "field": "x",
         "title": null,
         "type": "quantitative"
        },
        "y": {
         "field": "y",
         "title": null,
         "type": "quantitative"
        }
       },
       "height": 600,
       "mark": "bar",
       "title": "Imphal in 2018",
       "width": 1200
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABM8AAAKJCAYAAACsxg6FAAAABmJLR0QA/wD/AP+gvaeTAAAgAElEQVR4nOzde5DddX0//mdMItkQkAWJsAEZFrBKOmObAFo5mnxrwsUmBUZjJVTw1sQRvNHatSDGOhZdLFboxRItRZt6aexghQ4JBKV0FyFcatUgBV3lkg0EkgUCm5BL9/dHftnuZs872c3u2UvyeMxkJvv+fM7n9fpcz+5zPud8xnV1dXUFAAAAAOjjZSPdAAAAAACMVsIzAAAAACgQngEAAABAgfAMAAAAAAomjHQDAAD7q3HjxiVJ9vX5THt7/WCX3x87duxIS0tL1q1bl6OOOipvfvObM378+JrVAwAYbdx5BgAccMaNG9fr34Fq2bJlufDCC/OqV70qkydPzute97p89rOfzZYtW5IkmzZtyumnn5558+Zl2bJlmTdvXiqVSp5//vnuZbz00ku56667cuihh/bZlhs3bswll1yS448/PpMmTcoxxxyTiy66KI8//viwricAwGAIzwCAA07PO7VqeddWrXV1dQ2q/3e/+92ZNm1aWlpa8tRTT2XBggVZsmRJ/uRP/iRJctVVV+Wee+7J1VdfnZtvvjlXX3117r777lx33XXdy5g0aVJOP/30bNq0qc/y3/Wud+Vv//Zv88EPfjAbN27Mpz71qXzjG9/I29/+9n3uGQBguAnPAAD+f7vuRPu7v/u7HHfccWloaMjKlStz/fXX58QTT8y0adOyYsWKPvPffPPNmTFjRl7xilfkXe96V5577rley/3Wt76VU045JQcffHBOOeWU/Nd//Vf3tObm5vy///f/MmnSpBx99NE577zz8vDDDw+o391/3lO9ni666KJ8/vOfz0knnZRDDjkkTU1NSZJ/+Zd/SZL8+7//e5Jk7ty5SZK3vvWtvaYnew7wfvSjHyVJPvKRj2Ty5Ml597vfnSRZs2ZNv9YPAGA0EJ4BAOzmTW96U/75n/8569aty7nnnpsZM2bkn/7pn9Le3p5LL720z/yPPvpo7rjjjixevDjf+c538ulPf7rX9BdeeCErV67MV7/61dx///1ZvHhx97Qbb7wxV155ZTZs2JCLL7443/ve97pDpn21p3o93XDDDb1+3hWyTZ48OUnS3t6eJJk6dWqS5FWvelWS9Ptjl+973/uSJPfdd1+SpKWlJQcd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zJo1K7Zv397S6wAAAABwMphQr9frjQcffPDB2Lt3b/zkJz+J+++/Pzo6OuIHP/hBqdfXrl0bfX19R53vtNNOi4MHD1Z8KQAAAAAwNtOmTYtvfvObx75QL/Db3/62fvvtt9fr9Xr961//ev2xxx6r1+v1em9vb723tzf5esrChQubvl4VuXLlypUrV65cuXLlypUrV65cuXLHk1v4a5vXXXddLF++PL71rW/F888/H1/84hcjIqK7uzu6u7uTrwMAAADAyeTUooNTp04dbpR1d3fH1KlTIyKiq6ur6esAAAAAcDIpbJ5FRMyZMyfmzJlz1LFardb0dQAAAAA4mUz88Y9//OMcQbNnz84RI1euXLly5cqVK1euXLly5cqVK1du23IL/9omAAAAABBR+AcDAAAAAICMv7a5YcOGePzxx2Py5Mkxbdq0ynJef/312LRp0/CP2VWdu3Xr1njiiSdi1apVERExa9asLLn9/f3xu9/9LlauXBmnnXZazJw5M0vuSM8880zs2rUrZs+eXXnu2rVr4/HHH4++vr7o6+uLiMiSGxHxwQcfxJIlS+LgwYPZ7u/xvN7e3t548skn48CBA/HJT34yIvI8V+vWrYsnnngizjzzzOGMqnPL1IsqxtCYW3Ys7czNWbtG5uasXUXzHFF97RqZm3MtN15vrtr1n3K9uWpXY27VtauVtZojN6LaelWUm6NeFWXkqFfN5jmiunpVlJtj/aaut+p69Z92vVXXq1Ru1fWqlTWTIzei2npVlJujXhXl5qhXzeY5orp6VZSbY/2mrrfqevWfdr1V16tUbjvr1WjPZtnzZvnJs127dkWtVotNmzZFrVaL3bt3V5KzfPnyuPHGG6O7uztb7pYtW2Lbtm0xMDAQX/7yl2PVqlVZcvv7++Ott96Kd955J2688cZYvnx5tnmOiHj++efjpptuiu7u7iy53d3d8eyzz8bg4GAMDg7G/v37s+QePnw45s+fHy+++GLs27cvIvI8V/v37x++1meffTbWrFmTJbenpyduuummGBgYiJtuuimef/75LLmvvvpq3HDDDbF9+/aYP39+7Nq1q/LcMvWiijE05pYdS7tzc9WuxtxctatoniOqr12NublqV2NurtrVmJurdjXm5qpdjbk5alfZtZojt2gOcuTmqFdFGTnqVWqeI6qtV0W5OepVUW6OelWUm6NeFeXmqFdFuTnqVdk1kyM3ovp6VZSbo14V5eaoV6l5jqi2XhXl5qhXRbk56lVRbo56VZSbo14V5bazXo32bLZy3iw/efb000/HxIkTY/HixfG3v/0tTjnllLj44ovbnrNt27b4y1/+Ep2dnXHNNddkye3s7IxarRbz58+Pf/7zn7F379545513suZu27YtPvKRj8Rbb72VZZ43b94c3/72t+OGG26ISZMmxZ49eyrPXbVqVXR2dsZPf/rTqNVq0dnZmeX+9vb2xsqVK+PZZ5+Nzs7OiMjzPA/d36uvvjoeeuihePDBB6Onp6fy3Oeeey7OOuusePjhh2P79u3ZnqvHfc2EqwAAB71JREFUHnssOjs742c/+1ls27YtPvjgg9iyZUuluWXqxebNm9s+hsbcsmNpd26u2tUst8raVTTPOWpXY26u2tWYm6t2pe5v1bWrMTdX7WrMzVG7yq7Vdterotwrr7yy8npVlHvrrbdWXq9Gy62qXqXmuep6VZR78ODByutVUe7hw4crr1fN7m+V9aoo91//+lfl9aood+vWrVnrVbM1U2W9GsqdO3du1no1lLtgwYKs9aooN0e9GjnPOevVUO7evXuz1quh3H379mWtV433N1e9Gsp95513starodw33nijLfWqzLPZSj3K8pNnO3bsGP7xu1mzZsX27dsryanValGr1bLnRkQcPHgwVq9eHZ///OdjYGAgS+6aNWvizjvvjN27d8ftt9+eJXfv3r1x2223xW9+85v42Mc+FhH55rmvry8efPDB+NOf/hQRkeV6X3vttTj77LPjoYceipUrV2bLHbJkyZKo1Woxe/bsLPN88803x+rVq+OWW26JnTt3xs0335zlei+//PJYunRp/PCHP4yenp4YGBioPLdMvahizhtzy46lityI6mtXUW6O2tWYm6t2FV1vjtrVmJurdqWeq6prV2NurtrVmJuzdo22VnPkRhw7B7lyG4/lys211xqZ+95778Wtt94ajz766HC9ynW9ufZaI3Nz7rWKnqslS5bEF77whZg9e3aW3Jx7rZG5uepVmTWTIzciT70qyo2ovl4V5eaoV40ZuepV0fXmqFeNubnqVeq5qrpeNebmqleNue2oV2X3/q3sU7M0zyZMmBATJkw46t9Pttx77rkn7rvvvpg7d27lWUMOHDgQkyZNihdeeCFeeumlLLkPP/xwTJ48Of7whz8M/871iy++WHluV1dXzJ07N3bs2BFf+cpXYvXq1RFR/fXu3bs33njjjXj77bfjrrvuGi6SOe7v/v3746GHHop77713OLPq53nLli1x+eWXxy233BKvvPJKvPnmm5VljXTNNdfEr3/96zjnnHPiwgsvjMmTJ2fJHaloftWuaqhdale7/W+oXWXWao7cIrlyc9Srxoxc9Wpk7iOPPBJnnnlmLFu2bLhe9fX1VZ6bs16NzM1Zrxrv74cffhi/+MUv4r777ht+T9W5OevVyNxc9arsmsmRWyRXbtX1qig3R71qzMhVrxpzc9Wrxtxc9aroXuaoV425uepVY2476lXZvX/jPrWZU8tf0tjNmDEjenp6IuJIt2/OnDk5YrPkHj58OL7zne/EhRdeGDfeeGO23Ij/+a8pp5xySqxbty5L7hVXXBHvvvtuDA4OxocffhgRETNnzhzu0FaVO/K/HE2cODHb9c6YMSOuvfbaWLRoURw+fDjWr1+f7f4+/PDD8dWvfjWmT58+PJaqc9esWRMf//jH40tf+lL09PRET09Ptuu99tpr49prr41nnnkmLrnkkti2bVvWulF0nYcPH1a7KqB2qV3tdjLXrrJrtd31qii3SLvnuSg3R71KXW/V9aooN0e9KsrNUa9S97LqepW6v4888kh87Wtfq6xeFeXmqFep682x1yqzZqrYXzXmXn311ce8p4rPhcbcq666Ksv+quh6c+yvGjNy7a8ac++5554s+6uiOc2xvyq6v1XXq6LciMiyvyq63vHWq7LPZkv1qJ7Bzp0769OnT6/fdddd9enTp9d37txZSU5vb2+9VqvVa7Vavbe3N0vuz3/+8/pFF11UX7hwYX3hwoXZcnt7e+sLFy6sf//7369Pmzat/vrrr2eb5yEPPPBA/YEHHsh6vffcc0992rRp9ddeey1L7q5du+ozZ86s33333fUZM2bUX3nllSy57777bv3cc8+t79mzZ/hYjtyXXnqpftZZZ9Xvvvvu+vTp0+vr16/Pun5vu+22+rx58+qHDx+uPLdMvahiDI25ZcfS7txctasxN1ftKprnIVXWrtT1Vl27GnNz1a7G3Fy1qzE3V+1Krd8qa1fZtZojt2gOcuTmqFdFGTnqVWqeh1RVr5pdb5X1qig3R70qys1Rr4pyc9SrZuu3ynpVds3kyB06XmW9KsrNUa+KcnPUq9Q8D6mqXjW73irrVVFujnpVlJujXhXl5qhXzdZvu+pVs2ezlfNm+bXNqVOnRnd3d5x//vnR3d0dU6dOrSRn//79MXfu3Jg7d27s378/S+7FF18c119//VF/6SNH7owZM+KMM86ImTNnxsqVK2POnDnZ5nlIV1dXdHV1ZcmdPn16TJo0KWbOnBlr1qyJiy66KEvulClT4oUXXohZs2bFM888E5dddlmW3M2bN8eiRYuio6Nj+FiO3Hnz5sXy5cvjE5/4RCxbtiw+85nPZHuuTjnllJg7d24899xzMWHChMpzy9SLKsbQmFt2LO3OzVW7GnNz1a6ieR5SZe1qzM1Vuxpzc9WuxtxctasxN1ftKnquqq5dZddqjtyiOciRm6NeFWXkqFepeR5SVb0qys1Rr4pyc9Srotwc9aooN0e9Sj1XVdersmsmR25E9fWqKDdHvSrKzVGvUvM8pKp6VZSbo14V5eaoV0W5OepVUW6OepV6rtpZr5o9m62cd0K9Xq+P62oBAAAA4CSV5SfPAAAAAOBEpHkGAAAAAAmaZwAAAACQoHkGAAAAAAmaZwAAAACQ8P8ApEqdO9v/QNkAAAAASUVORK5CYII=",
      "image/svg+xml": [
       "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n",
       "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n",
       "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" class=\"marks\" width=\"1231\" height=\"649\" viewBox=\"0 0 1231 649\"><rect width=\"1231\" height=\"649\" fill=\"white\"/><g fill=\"none\" stroke-miterlimit=\"10\" transform=\"translate(25,27)\"><g class=\"mark-group role-frame root\" role=\"graphics-object\" aria-roledescription=\"group mark container\"><g transform=\"translate(0,0)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0.5,0.5h1200v600h-1200Z\" stroke=\"#ddd\"/><g><g class=\"mark-group role-axis\" aria-hidden=\"true\"><g transform=\"translate(0.5,600.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-grid\" pointer-events=\"none\"><line transform=\"translate(0,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(30,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(60,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(90,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(120,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(150,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(180,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(210,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(240,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(270,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(300,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(330,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(360,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(390,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(420,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(450,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(480,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(510,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(540,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(570,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(600,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(630,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(660,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(690,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(720,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(750,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(780,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(810,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(840,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(870,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(900,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(930,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(960,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(990,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1020,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1050,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1080,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1110,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1140,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1170,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1200,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-group role-axis\" aria-hidden=\"true\"><g transform=\"translate(0.5,0.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-grid\" pointer-events=\"none\"><line transform=\"translate(0,600)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,557)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,514)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,471)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,429)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,386)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,343)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,300)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,257)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,214)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,171)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,129)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,86)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,43)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,0)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-group role-axis\" role=\"graphics-symbol\" aria-roledescription=\"axis\" aria-label=\"X-axis for a linear scale with values from 0 to 400\"><g transform=\"translate(0.5,600.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-tick\" pointer-events=\"none\"><line transform=\"translate(0,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(30,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(60,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(90,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(120,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(150,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(180,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(210,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(240,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(270,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(300,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(330,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(360,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(390,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(420,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(450,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(480,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(510,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(540,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(570,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(600,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(630,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(660,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(690,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(720,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(750,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(780,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(810,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(840,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(870,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(900,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(930,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(960,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(990,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1020,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1050,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1080,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1110,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1140,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1170,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1200,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g><g class=\"mark-text role-axis-label\" pointer-events=\"none\"><text text-anchor=\"start\" transform=\"translate(0,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0</text><text text-anchor=\"middle\" transform=\"translate(30,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">10</text><text text-anchor=\"middle\" transform=\"translate(60,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">20</text><text text-anchor=\"middle\" transform=\"translate(90,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">30</text><text text-anchor=\"middle\" transform=\"translate(120,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">40</text><text text-anchor=\"middle\" transform=\"translate(150,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">50</text><text text-anchor=\"middle\" transform=\"translate(180,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">60</text><text text-anchor=\"middle\" transform=\"translate(210,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">70</text><text text-anchor=\"middle\" transform=\"translate(240,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">80</text><text text-anchor=\"middle\" transform=\"translate(270,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">90</text><text text-anchor=\"middle\" transform=\"translate(300,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">100</text><text text-anchor=\"middle\" transform=\"translate(330,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">110</text><text text-anchor=\"middle\" transform=\"translate(360,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">120</text><text text-anchor=\"middle\" transform=\"translate(390,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">130</text><text text-anchor=\"middle\" transform=\"translate(420,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">140</text><text text-anchor=\"middle\" transform=\"translate(450,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">150</text><text text-anchor=\"middle\" transform=\"translate(480,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">160</text><text text-anchor=\"middle\" transform=\"translate(510,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">170</text><text text-anchor=\"middle\" transform=\"translate(540,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">180</text><text text-anchor=\"middle\" transform=\"translate(570,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">190</text><text text-anchor=\"middle\" transform=\"translate(600,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">200</text><text text-anchor=\"middle\" transform=\"translate(630,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">210</text><text text-anchor=\"middle\" transform=\"translate(660,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">220</text><text text-anchor=\"middle\" transform=\"translate(690,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">230</text><text text-anchor=\"middle\" transform=\"translate(720,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">240</text><text text-anchor=\"middle\" transform=\"translate(750,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">250</text><text text-anchor=\"middle\" transform=\"translate(780,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">260</text><text text-anchor=\"middle\" transform=\"translate(810,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">270</text><text text-anchor=\"middle\" transform=\"translate(840,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">280</text><text text-anchor=\"middle\" transform=\"translate(870,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">290</text><text text-anchor=\"middle\" transform=\"translate(900,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">300</text><text text-anchor=\"middle\" transform=\"translate(930,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">310</text><text text-anchor=\"middle\" transform=\"translate(960,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">320</text><text text-anchor=\"middle\" transform=\"translate(990,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">330</text><text text-anchor=\"middle\" transform=\"translate(1020,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">340</text><text text-anchor=\"middle\" transform=\"translate(1050,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">350</text><text text-anchor=\"middle\" transform=\"translate(1080,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">360</text><text text-anchor=\"middle\" transform=\"translate(1110,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">370</text><text text-anchor=\"middle\" transform=\"translate(1140,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">380</text><text text-anchor=\"middle\" transform=\"translate(1170,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">390</text><text text-anchor=\"end\" transform=\"translate(1200,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">400</text></g><g class=\"mark-rule role-axis-domain\" pointer-events=\"none\"><line transform=\"translate(0,0)\" x2=\"1200\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-group role-axis\" role=\"graphics-symbol\" aria-roledescription=\"axis\" aria-label=\"Y-axis for a linear scale with values from 0 to 7\"><g transform=\"translate(0.5,0.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-tick\" pointer-events=\"none\"><line transform=\"translate(0,600)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,557)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,514)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,471)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,429)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,386)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,343)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,300)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,257)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,214)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,171)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,129)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,86)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,43)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,0)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g><g class=\"mark-text role-axis-label\" pointer-events=\"none\"><text text-anchor=\"end\" transform=\"translate(-7,603)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.0</text><text text-anchor=\"end\" transform=\"translate(-7,560.1428571428571)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.5</text><text text-anchor=\"end\" transform=\"translate(-7,517.2857142857143)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">1.0</text><text text-anchor=\"end\" transform=\"translate(-7,474.42857142857144)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">1.5</text><text text-anchor=\"end\" transform=\"translate(-7,431.57142857142856)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">2.0</text><text text-anchor=\"end\" transform=\"translate(-7,388.71428571428567)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">2.5</text><text text-anchor=\"end\" transform=\"translate(-7,345.85714285714283)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">3.0</text><text text-anchor=\"end\" transform=\"translate(-7,303)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">3.5</text><text text-anchor=\"end\" transform=\"translate(-7,260.14285714285717)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">4.0</text><text text-anchor=\"end\" transform=\"translate(-7,217.28571428571425)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">4.5</text><text text-anchor=\"end\" transform=\"translate(-7,174.42857142857142)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">5.0</text><text text-anchor=\"end\" transform=\"translate(-7,131.57142857142858)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">5.5</text><text text-anchor=\"end\" transform=\"translate(-7,88.71428571428574)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">6.0</text><text text-anchor=\"end\" transform=\"translate(-7,45.85714285714284)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">6.5</text><text text-anchor=\"end\" transform=\"translate(-7,3)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">7.0</text></g><g class=\"mark-rule role-axis-domain\" pointer-events=\"none\"><line transform=\"translate(0,600)\" x2=\"0\" y2=\"-600\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-rect role-mark marks\" role=\"graphics-object\" aria-roledescription=\"rect mark container\"><path aria-label=\"x: 8; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M21.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 10; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M27.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 14; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M39.50000000000001,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 15; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M42.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 16; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M45.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 18; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M51.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 20; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M57.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 22; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M63.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 26; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M75.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 27; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M78.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 29; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M84.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 30; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M87.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 31; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M90.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 35; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M102.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 36; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M105.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 37; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M108.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 57; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M168.49999999999997,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 58; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M171.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 64; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M189.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 65; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M192.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 66; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M195.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 70; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M207.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 72; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M213.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 78; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M231.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 80; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M237.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 81; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M240.50000000000003,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 91; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M270.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 94; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M279.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 96; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M285.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 97; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M288.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 98; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M291.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 99; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M294.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 101; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M300.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 102; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M303.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 104; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M309.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 105; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M312.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 106; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M315.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 108; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M321.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 109; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M324.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 110; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M327.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 112; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M333.50000000000006,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 113; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M336.49999999999994,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 114; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M339.49999999999994,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 115; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M342.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 116; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M345.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 117; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M348.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 119; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M354.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 121; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M360.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 123; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M366.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 124; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M369.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 126; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M375.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 127; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M378.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 128; y: 4\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M381.5,257.14285714285717h5v342.85714285714283h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 129; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M384.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 130; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M387.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 131; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M390.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 132; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M393.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 133; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M396.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 134; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M399.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 136; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M405.50000000000006,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 140; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M417.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 141; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M420.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 142; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M423.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 144; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M429.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 145; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M432.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 149; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M444.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 154; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M459.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 155; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M462.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 156; y: 4\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M465.5,257.14285714285717h5v342.85714285714283h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 158; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M471.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 159; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M474.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 160; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M477.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 161; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M480.50000000000006,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 162; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M483.50000000000006,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 170; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M507.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 171; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M510.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 172; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M513.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 173; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M516.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 176; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M525.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 179; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M534.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 180; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M537.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 181; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M540.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 182; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M543.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 184; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M549.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 185; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M552.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 186; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M555.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 187; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M558.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 188; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M561.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 189; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M564.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 191; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M570.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 193; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M576.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 194; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M579.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 195; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M582.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 196; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M585.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 197; y: 6\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M588.5,85.71428571428574h5v514.2857142857142h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 198; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M591.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 199; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M594.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 200; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M597.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 201; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M600.4999999999999,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 203; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M606.4999999999999,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 204; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M609.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 207; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M618.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 208; y: 5\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M621.5,171.42857142857142h5v428.57142857142856h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 209; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M624.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 210; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M627.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 211; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M630.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 212; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M633.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 213; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M636.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 214; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M639.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 215; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M642.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 216; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M645.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 217; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M648.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 218; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M651.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 219; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M654.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 220; y: 6\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M657.5,85.71428571428574h5v514.2857142857142h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 221; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M660.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 222; y: 4\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M663.5000000000001,257.14285714285717h5v342.85714285714283h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 223; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M666.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 225; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M672.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 227; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M678.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 230; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M687.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 232; y: 7\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M693.5,0h5v600h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 234; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M699.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 235; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M702.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 236; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M705.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 237; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M708.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 238; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M711.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 241; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M720.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 244; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M729.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 245; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M732.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 248; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M741.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 249; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M744.5000000000001,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 250; y: 3\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M747.5,342.85714285714283h5v257.14285714285717h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 252; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M753.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 254; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M759.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 259; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M774.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 260; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M777.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 262; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M783.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 263; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M786.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 266; y: 4\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M795.5,257.14285714285717h5v342.85714285714283h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 268; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M801.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 269; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M804.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 270; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M807.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 271; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M810.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 275; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M822.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 276; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M825.4999999999999,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 278; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M831.4999999999999,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 279; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M834.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 282; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M843.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 291; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M870.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 292; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M873.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 296; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M885.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 300; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M897.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 303; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M906.4999999999999,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 305; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M912.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 306; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M915.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 307; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M918.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 310; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M927.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 311; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M930.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 314; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M939.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 316; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M945.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 319; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M954.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 320; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M957.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 331; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M990.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 333; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M996.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 335; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1002.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 336; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1005.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 337; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1008.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 339; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1014.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 341; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1020.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 342; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1023.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 345; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1032.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 346; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1035.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 348; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1041.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 350; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1047.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 354; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1059.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 355; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1062.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 356; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1065.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 357; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1068.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 359; y: 1\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1074.5,514.2857142857143h5v85.71428571428567h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 360; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1077.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"x: 362; y: 2\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1083.5,428.57142857142856h5v171.42857142857144h-5Z\" fill=\"#4c78a8\"/></g><g class=\"mark-group role-title\"><g transform=\"translate(600,-22)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-text role-title-text\" role=\"graphics-symbol\" aria-roledescription=\"title\" aria-label=\"Title text 'Imphal in 2018'\" pointer-events=\"none\"><text text-anchor=\"middle\" transform=\"translate(0,10)\" font-family=\"sans-serif\" font-size=\"13px\" font-weight=\"bold\" fill=\"#000\" opacity=\"1\">Imphal in 2018</text></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" display=\"none\"/></g></g></g></svg>\n"
      ],
      "text/plain": [
       "@vlplot(\n",
       "    height=600,\n",
       "    width=1200,\n",
       "    title=\"Imphal in 2018\",\n",
       "    mark=\"bar\",\n",
       "    encoding={\n",
       "        x={\n",
       "            field=\"x\",\n",
       "            title=nothing\n",
       "        },\n",
       "        y={\n",
       "            field=\"y\",\n",
       "            title=nothing\n",
       "        }\n",
       "    },\n",
       "    data={\n",
       "        values=...\n",
       "    }\n",
       ")"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(plot)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "027d8056-10a2-44b3-94d0-5c0daa55180e",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "210f2d79-516c-423f-820d-8c347649c2e7",
   "metadata": {},
   "source": [
    "## Wstępne modelowanie predykcyjne"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3af3c616-a686-4a2a-876f-b6934b9dce68",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b839da96-de24-4066-8f4a-a7527711a30a",
   "metadata": {},
   "outputs": [],
   "source": [
    "model_data = DataFrame(t=dat[1], n=dat[2]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7429ee21-549e-4963-ab61-f21188bf56df",
   "metadata": {},
   "outputs": [],
   "source": [
    "md = DataFrame(t=Int64[], n=Int64[])\n",
    "for day in 1:(leap ? 366 : 365)\n",
    "    push!(md, day in model_data.t ? Matrix(model_data[in(day).(model_data.t), :]) : [day, 0])\n",
    "end;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6cad00a2-06a4-4136-a606-ad9344862bed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>8 rows × 2 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>n</th><th>nrow</th></tr><tr><th></th><th title=\"Int64\">Int64</th><th title=\"Int64\">Int64</th></tr></thead><tbody><tr><th>1</th><td>0</td><td>183</td></tr><tr><th>2</th><td>1</td><td>103</td></tr><tr><th>3</th><td>2</td><td>53</td></tr><tr><th>4</th><td>3</td><td>18</td></tr><tr><th>5</th><td>4</td><td>4</td></tr><tr><th>6</th><td>5</td><td>1</td></tr><tr><th>7</th><td>6</td><td>2</td></tr><tr><th>8</th><td>7</td><td>1</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|cc}\n",
       "\t& n & nrow\\\\\n",
       "\t\\hline\n",
       "\t& Int64 & Int64\\\\\n",
       "\t\\hline\n",
       "\t1 & 0 & 183 \\\\\n",
       "\t2 & 1 & 103 \\\\\n",
       "\t3 & 2 & 53 \\\\\n",
       "\t4 & 3 & 18 \\\\\n",
       "\t5 & 4 & 4 \\\\\n",
       "\t6 & 5 & 1 \\\\\n",
       "\t7 & 6 & 2 \\\\\n",
       "\t8 & 7 & 1 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m8×2 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m n     \u001b[0m\u001b[1m nrow  \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Int64 \u001b[0m\u001b[90m Int64 \u001b[0m\n",
       "─────┼──────────────\n",
       "   1 │     0    183\n",
       "   2 │     1    103\n",
       "   3 │     2     53\n",
       "   4 │     3     18\n",
       "   5 │     4      4\n",
       "   6 │     5      1\n",
       "   7 │     6      2\n",
       "   8 │     7      1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mod = combine(groupby(md, :n), nrow)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "18794b69-ada5-45d7-b6e0-2dcf5fad808a",
   "metadata": {},
   "outputs": [],
   "source": [
    "sum(mod[!,2]) |> sum -> mod[!,2] ./= sum;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f679c8da-c0fa-402c-98d7-90b1e1506854",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.vegalite.v4+json": {
       "data": {
        "values": [
         {
          "n": 0,
          "nrow": 0.5013698630136987
         },
         {
          "n": 1,
          "nrow": 0.2821917808219178
         },
         {
          "n": 2,
          "nrow": 0.14520547945205478
         },
         {
          "n": 3,
          "nrow": 0.049315068493150684
         },
         {
          "n": 4,
          "nrow": 0.010958904109589041
         },
         {
          "n": 5,
          "nrow": 0.0027397260273972603
         },
         {
          "n": 6,
          "nrow": 0.005479452054794521
         },
         {
          "n": 7,
          "nrow": 0.0027397260273972603
         }
        ]
       },
       "encoding": {
        "x": {
         "field": "n",
         "type": "quantitative"
        },
        "y": {
         "field": "nrow",
         "type": "quantitative"
        }
       },
       "height": 600,
       "mark": "bar",
       "title": "Poisson-styled reprezentation of data",
       "width": 1200
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABOMAAAKYCAYAAAAxLTzlAAAABmJLR0QA/wD/AP+gvaeTAAAgAElEQVR4nOzdfZRWZbk/8C82jLxIQqkgYiqi4kt6NMyC8R18WadEPU1Le7Ny5SlTWWpFucyDulIn6yS9aAtLy1VaSaWhlYplOmOWcsQKK1QyTRABRwQFEd2/P/wxOTAwaM/co0+fz1osmXvve1/39czzB37XvffuU1VVFQAAAACgx23S2wsAAAAAgH8XwjgAAAAAKEQYBwAAAACFCOMAAAAAoBBhHADQo/r06ZM+ffr09jKKqEWv/06fVwmvhc9z9uzZGTNmTBobGzNgwICNmvNaWDcA0DOEcQDAeq0JBPr06ZOGhoaMGDEiJ598ctrb23t7acUIRXrPq/nsX4u/r5NPPjmzZs3KL37xizz77LM9UuO12DcA0DVhHADQraqq8sQTT+Too4/OZZddlhNPPPEVza2qqgdXB+v3Wvj+3XfffUmS/fffv1fXAQC8NgjjAICN8qY3vSlTpkxJktx0000d4y+++GKmTp2a0aNHZ+DAgdl1110zderUvPjii0nW3bGzcOHCnHTSSdluu+3Sv3//vPOd78z555/f7bGNrXPNNddkzJgxGThwYMaMGZN77713g31tqObL1/3yXYIf/OAHO11jn3326XJX0v33359jjz02W2+9dTbddNNsu+22OeWUU7Js2bKOnr7yla9kxx13zMCBA3PEEUdscK1r6l9//fXZe++909DQsFF11sy74YYbss8++2TzzTfPcccdl6VLl9bkui//84Y3vOEVzV3f76urzz5JWlpacvDBB6dfv37Zeuutc8wxx2Tu3Lkb/H29fLzW36ONud6a3XCbbrrpeq/R3ffglfbd3RwAoBdVAADrkaR6+T8XnnjiiSpJtd1223WMXXLJJVWS6swzz6yWL19enXnmmVWSaurUqV1eY9y4cVWS6qabbqpWrFhR/frXv67e8Y53dHtsY+tMmzatWrx4cfX973+/SlLtu+++G+xxQzXXXv+zzz5bbbnlltWmm25aLVq0qKqqqpo7d26VpBo2bNg6vU6YMKFKUp1++unV008/XX3hC1+oklSnnHJKVVVV9aEPfahKUp199tnVsmXLqgULFqxzja5+Hy//szF11pz79a9/vVq6dGn16U9/ukpSnXbaaf/SdV/uggsu6OjllaxpQ7+vrj6L/fbbr7rzzjur5cuXV+eff36VpHr729++3jlr/1zr71F311tfHy+3Md+DV9r3xswBAHqHMA4AWK+X/w/+E088UZ133nlVkuqLX/xixzm77LJLlaR65JFHqqqqqn/84x9VkmrXXXdd5xpVVVWbb755RygzY8aMqr29faOOvdI6zz77bJWkamxs7HR87cBpQzW7uu4555xTJalaWlqqqqo6QqbPfOYz65w7ePDgKkn15JNPVlVVVe3t7VWSasSIEVVVVdVOO+1UJakWLly43npdreWee+6pVqxYsdF11r7m/PnzO4Wqr/a6a9x2221VQ0NDdfDBB1erV69+VWta+/fV3WdRVVX1zDPPVH369KkaGhrWO2ftn//V79HaurvexvTxSr8HG9P3xswBAHpHn6ryEBcAoGsvv/2tsbExo0aNyqGHHppLLrkkm2zy0tMuBg4cmGeffTbPPfdcGhsbs2rVqmy66aYZMGBAnnnmmY5rrPknx9e//vWceeaZWbVqVZJk2LBhueaaa3LQQQdt8NgrrfPy9W/onzsbqtnVNRYuXJjtt98+22yzTebOnZt99tkn9913X/785z9n11137XRuQ0NDXnjhhS4/1xdffDEDBgzIihUrsmrVqvTt27fbNa/vWHd11p635rPr169fVqxY8aqvu+bz2HvvvVNVVe69994MGzbsVa2pq/7W/nnBggX52te+ljvvvDMPPvhgnnzyyaxYsWKDc9b+udbfo+6u1938JN1+D15N3xszBwDoHZ4ZBwB0q6qqPPfcc5kzZ06++tWvdgRxSfKWt7wlSbJo0aIkyeLFi5Mk2223XZfXOuWUUzJ//vxcd911+eQnP5nHH388xx57bLfHXmmdjbWhmkk6np+2JnwaOnRo3v/+9+ehhx7K17/+9dx3330ZN25cRo8evc61Bw0a1LHm6v+/SKCqqo5rbbXVVkmSJ5988l/qobs6a1uyZEmSZMSIEf/SdV944YW8733vyxNPPJGrr766I4h7NWvqytqf/eGHH54LL7wwEyZMyK9//euO78CG5qyt1t+jWlyvu+/Bq+l7Y+YAAL1DGAcA/Es+8YlPJEkuueSSLFu2LJdcckmS5OMf/3iX548bNy6zZ8/OhAkTctRRRyVJ9thjj26PvdI6G2tDNZNk5MiRSZK2traOsdNPPz19+vTJ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zz03/fv3zwc/+MGcccYZ2WWXXUqsDQAAAADqSrdh3Mc+9rEMHTo0t9xyS374wx/m8ssvz+jRo3Puueemubm5xBoBNtp5370j85csS5I8//zz6dv3L/mfEw7I1m/erJdXBgAAABtxm+qaZ8Q1NDRk7733Tr9+/fLnP/85c+bMKbE+gFfk8SeX57FFy/LYomV54qmVeWzRstqcB9MAACAASURBVDy/+oXeXhYAAAAk2YidcXfffXeuuOKKjp8HDRqUvffeOzvvvHOPLgwAAAAA6k23YdyECRMyatSo7Ljjjtlxxx2z1VZblVgXAAAAANSdbm9THTduXI477rg89thj+e53v5vp06fn+eefL7E2AAAAAKgr3e6MW716dQ488MDceeedHWPveMc7cvvtt6dv3749ujgAAAAAqCfdhnHXXXddZs+enY985CPZaqut8uSTT+bqq6/O9ddfn/e85z0l1ggAAAAAdaHbMG7evHn52Mc+lksuuaRjrH///vnb3/7WowsDAAAAgHrTbRg3cuTInHvuuVm2bFm23HLLLF68ONdcc02uuuqqEusDAAAAgLrRbRg3ceLE7LXXXrniiis6xsaOHZuJEyf26MIAAAAAoN50G8b17ds3t99+e6677ro8/PDD2WGHHTJx4sQ0NHQ7FQAAAAB4mW4Ttba2trS2tmbcuHFe2AAAAAAA/4JNujuhvb0955xzTm688cYS6wEAAACAutXtzrjBgwdn9OjR+dnPfpbBgwd3jI8bNy5NTU09ujgAAAAAqCfdhnEzZ87MH/7whyTJZz/72Y7x//mf/xHGAQAAAMAr0G0Y19TUlMmTJ3c5DgAAAABsvG7DuPHjx2ezzTZLW1tbVq9e3THer1+/Hl0YAAAAANSbjXqb6v7775+qqjqNu00VAAAAAF6ZbsO43/72txk6dGiOP/74NDY2dowL4gAAAADglek2jBszZkw+8IEP5OKLLy6xHgAAAACoW92GcQ0NDbnjjjvS0tLSaXzcuHF2xwEAAADAK9BtGDdz5sz87ne/y+9+97tO454ZBwAAAACvTLdhXFNTUyZPntzlOAAAAACw8boN48aPH5/x48eXWAsAAAAA1LVNensBAAAAAPDvQhgHAAAAAIUI4wAAAACgEGEcAAAAABQijAMAAACAQoRxAAAAAFCIMA4AAAAACmnoiYuuWrUqDz74YHbaaaf07du307GqqvK3v/0ty5Yty0477ZQBAwZk/vz5WbBgQcc5W2+9dYYPH94TSwMAAACAXlPzMO65557Lfvvtl2eeeSaDBg3KXXfdlcbGxo7jV1xxRS677LKsWrUqTzzxRFpbW/O9730v06ZN6wjgTjrppJx00km1XhoAAAAA9Kqa36Z6yy23ZJtttskDDzyQrbbaKrfeemun4yeeeGLuueee/OEPf8i73vWuXHfddUleCuDuueee3HPPPYI4AAAAAOpSzcO4Bx98MHvuuWeSZK+99srcuXPXe+7jjz+enXbaKUmyYMGCzJ49OytXrqz1kgAAAADgNaFPVVVVLS94wQUXZOXKlTnvvPPy+c9/PgMGDMjnPve5dc676qqr8tvf/jaXXnppLr/88kybNi0rVqzIk08+mdbW1uy4445JktbW1rS1ta0zv7m5uZbL5nXo8fYVuXD6nzqNDR3cL2c1v7WXVsRrwQXX/jELn+oc6n/uPXtk2JD+vbQiAAAA/l2NHDlynbGaPzPuzW9+c+bMmZMkaW9vz1ve8pYkyfz585Mkw4cPz09+8pPccccdufzyy5N0fkbcxz/+8fzsZz/L6aefniRpampKU1NTpxotLS1dNtMT5s2bV6RWqTr1VKth4dIkncO4xsbGHu+tXj6/3qhTolZj41+TdA7jRowYkbcM3bzHatbT59cbteqxp5K16rGnkrXqsaeSteqxp5K16rGnkrXqsaeSteqxp5K16rGnkrXqsaeSteqxp5K1SvfUlZqHcQceeGAuuOCCHHLIIZkxY0ZOPfXUJMm0adOSvHTr6rnnnptLL700s2bNytZbb53kpdtUlyxZkjvuuCMTJ06s9bIAAAAAoNfVPIwbPXp0zjnnnFx++eU555xzsssuuyRJx5tSFy1alL59+2bSpElJXtoVt9122+VrX/taVq9enVNPPTVHHnlkrZcFAAAAAL2u5mFc8tIbU0888cROYy9/Q2pXb0s9/PDDe2IpAAAAAPCaUfO3qQIAAAAAXRPGAQAAAEAhwjgAAAAAKEQYBwAAAACFCOMAAAAAoBBhHAAAAAAUIowDAAAAgEKEcQAAAABQiDAOAAAAAAoRxgEAAABAIcI4AAAAAChEGAcAAAAAhQjjAAAAAKAQYRwAAAAAFCKMAwAAAIBChHEAAAAAUIgwDgAAAAAKEcYBAAAAQCHCOAAAAAAoRBgHAAAAAIUI4wAAAACgEGEcAAAAABQijAMAAACAQoRxAAAAAFCIMA4AAAAAChHGAQAAAEAhwjgAAAAAKEQYBwAAAACFCOMAAAAAoBBhHAAAAAAUIowDAAAAgEKEcQAAAABQiDAOAAAAAAoRxgEAAABAIcI4AAAAAChEGAcAAAAAhQjjAAAAAKAQYRwAAAAAFCKMAwAAAIBChHEAAAAAUIgwDgAAAAAKEcYBAAAAQCHCOAAAAAAoRBgHAAAAAIUI4wAAAACgEGEcAAAAABTSI2Hc9ddfnw9/+MOZMWPGOsfuuuuufOITn8j73//+fPOb30xVVd3OAQAAAIB6UPMw7uGHH84nPvGJjB07Nv/93/+dRx55pNPxQYMG5ZBDDskRRxyRL33pS5k+fXq3cwAAAACgHjTU+oIzZ87M0UcfnZNOOimzZs3Krbfemo985CMdx3fffffsvvvuSZK77747jz76aJYuXbrBOQAAAABQD2q+M27RokV585vfnCTZaqutsnDhwi7Pa29vz8yZM3PMMcds9BwAAAAAeD3rU615aFuN/O///m+WLFmSL3zhC/nc5z6XrbbaKqeffnqnc5577rmccMIJOfvss7PHHntscE5ra2va2trWqdPc3FzLZfM69Hj7ilw4/U+dxoYO7pezmt/aSyviteCCa/+YhU+t7DT2uffskWFD+vfSigAAAPh3NXLkyHXGan6b6vbbb98Rnv31r3/NfvvtlyS59tprkySHH354jjvuuJx66qnZY489NjgnSZqamtLU1NSpRktLS5fN9IR58+YVqVWqTj3Vali4NEnnMK6xsbHHe6uXz6836pSo1dj41ySdw7gRI0bkLUM377Ga9fT59UateuypZK167KlkrXrsqWSteuypZK167KlkrXrsqWSteuypZK167KlkrXrsqWSteuypZK3SPXWl5repHn744fnDH/6Qpqam/PGPf8xhhx2WJJkzZ07mzJmTqVOnZu7cubnyyivz3ve+N9dee+165wAAAABAPan5zriBAwfm97//fWbPnp299947AwYMSNL5ttLRo0d3/H233XZb7xwAAAAAqCc1D+OSZMiQITn44IM7ja15g+raf9/QHAAAAACoJzW/TRUAAAAA6JowDgAAAAAKEcYBAAAAQCHCOAAAAAAoRBgHAAAAAIUI4wAAAACgEGEcAAAAABQijAMAAACAQoRxAAAAAFCIMA4AAAAAChHGAQAAAEAhwjgAAAAAKEQYBwAAAACFCOMAAAAAoBBhHAAAAAAUIowDAAAAgEKEcQAAAABQiDAOAAAAAAoRxgEAAABAIcI4AAAAAChEGAcAAAAAhQjjAAAAAKAQYRwAAAAAFCKMAwAAAIBChHEAAAAAUIgwDgAAAAAKEcYBAAAAQCHCOAAAAAAoRBgHAAAAAIUI4wAAAACgEGEcAAAAABQijAMAAACAQoRxAAAAAFCIMA4AAAAAChHGAQAAAEAhwjgAAAAAKEQYBwAAAACFCOMAAAAAoBBhHAAAAAAUIowDAAAAgEKEcQAAAABQiDAOAAAAAAoRxgEAAABAIcI4AAAAAChEGAcAAAAAhTT01IUXL16cLbbYYr3Hn3nmmaxatSpDhgxJe3t72tvbO44NGTIkQ4YM6amlAQAAAECvqPnOuNWrV+eggw7KqFGjcuihh2b16tXrnLNgwYKceuqpmTp1apJk6tSpGTNmTCZMmJAJEybkqquuqvWyAAAAAKDX1TyM+9WvfpU+ffrkqaeeyurVq3P77bevc86PfvSjXHfddZ3GTjvttDz00EN56KGHMmnSpFovCwAAAAB6Xc1vU/3zn/+ct7/97UmS/fbbL3PmzMkhhxzS6ZxJkyZ1ui01Sdrb2/PYY49l6623ziabeJQdAAAAAPWnT1VVVS0veMEFF2TlypU577zzcs4556Rfv34566yz1jlvypQpHf+dOnVqvvrVr+bpp5/OFltskZkzZ2abbbZJkrS2tqatrW2d+c3NzbVcNq9Dj7evyIXT/9RpbOjgfjmr+a29tCJeCy649o9Z+NTKTmOfe88eGTakfy+tCAAAgH9XI0eOXGes5jvjhgwZkrlz5yZJli5dmuHDhydJx064rl7MMGnSpEyaNClVVeWEE07I9OnTO25VbWpqSlNTU6fzW1paumymJ8ybN69IrVJ16qlWw8KlSTqHcY2NjT3eW718fr1Rp0Stxsa/Jukcxo0YMSJvGbp5j9Wsp8+vN2rVY08la9VjTyVr1WNPJWvVY08la9VjTyVr1WNPJWvVY08la9VjTyVr1WNPJWvVY08la5XuqSs1vx907NixufHGG3PXXXfll7/8ZcaOHZvkpZc0rHlhw5q3p778z7x58zJ79uz85S9/ybbbblvrZQEAAABAr6v5zri99torH/7wh/PJT34yJ5xwQvbcc88knXfEXXXVVbnhhhuSvLRdb9ttt81FF12UVatW5eijj84xxxxT62UBAAAAQK+reRiXJGedddY6z4l7+RtS19yW+nLHHntsTywFAAAAAF4zeiSMA4DXigf+8WQefOyl55YuXrw4f11UZdQ2Q7LTiDf18soAAIB/R8I4AOra3X+Zn2tunfOykYdz/KG7C+MAAIBeUfMXOAAAAAAAXRPGAQAAAEAhwjgAAAAAKEQYBwAAAACFCOMAAAAAoBBhHAAAAAAUIowDAAAAgEKEcQAAAABQiDAOAAAAAAoRxgEAAABAIcI4AAAAAChEGAcAAAAAhQjjAAAAAKAQYRwAAAAAFCKMAwAAAIBChHEAAAAAUIgwDgAAAAAKEcYBAAAAQCHCOAAAAAAoRBgHAAAAAIUI4wAAAACgEGEcAAAAABQijAMAAACAQoRxAAAAAFCIMA4AAAAAChHGAQAAAEAhwjgAAACA/9fenUdXVZ3/H//EAAIyliEYCCoslamWURQClmXAOMJCKBBtitLaqpA2WqWglaCVb0KBONHVUqK/1jJYsGIBGyAokASwCiqDVawRKiCBC5EEyJz9+4N1Yy73ZsJkn3uP79darBXOvpfn2eFhH/aTc84FLKEZBwAAAAAAAFhCMw4AAAAAAACwhGYcAAAAAAAAYAnNOAAAAAAAAMASmnEAAAAAAACAJTTjAAAAAAAAAEtoxgEAAAAAAACW0IwDAAAAAAAALKEZBwAAAAAAAFhCMw4AAAAAAACwhGYcAAAAAAAAYAnNOAAAAAAAAMASmnEAAAAAAACAJTTjAAAAAAAAAEtoxgEAAAAAAACW0IwDAAAAAAAALKEZBwAAAAAAAFjSKM24rKwszZo1S9nZ2dW+ZseOHVq7dm293gMAAAAAAACEsgZvxh09elQTJkxQy5Ytdffdd+vYsWN+r3n99dc1ceJE7dq1q87vAQAAAAAAAEJdgzfjNm7cqLvuuku//e1vdfvtt2vTpk1+r7nyyis1YMCAer0HAAAAAAAACHUN3ozLzc1VRESEJOnyyy/X0aNH/V4zaNAgDRo0qF7vAQAAAAAAAEJdk4b+A8PDwyu/rqioUNOmTb/Ve7KysgI+Ry4nJ+dbZlp3tmK5cU6NGetYXqHfsZKSEitzc8P3z6k4jR2rpKTE79jhw4dVdvZko8WU3PP9cypWY8bJy8sLeMxNa4Uba8JmLDfOyWYsN87JZiw3zslmLDfOyWYsN87JZiw3zslmLDfOyWYsN87JZiybcwqkwZtxUVFR2r17tyTp4MGDlbejej+s4c4776zzeyQpOjpa0dHRPq9PSUlRjx49Gjr1gHJycqzEshXHTbGa5J6WtM/nWLNmzRp9bm75/jkRx0asZs0+lVTkc6xbt27qHtG20WK66fvnRKzGjtM+55wk3yuu27dv75q1wo01YTOWG+dkM5Yb52QzlhvnZDOWG+dkM5Yb52QzlhvnZDOWG+dkM5Yb52Qzlu05BdLgt6nGxsYqMzNTEydOVGZmpsaMGSNJ2rVrV+UHNqxdu1br1q3TunXrtHbt2mrfAwAAAAAAALhJg18Z17ZtW23fvl2ZmZlKTU1V27bnr0apekVcZGSkHnjggcqvq3sPAAAAAAAA4CYN3oyTzt92GhcX53Os6gc2XPgBDtW9BwAAAAAAAHCTBr9NFQAAAAAAAEBgNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWNKksf7giooKXXJJ9b2+quOFhYUqKiqqHGvevLlatGjRWKkBAAAAAAAAjmjwK+MqKio0adIktWzZUlOmTFFFRUWt4ykpKYqMjFTPnj3Vs2dPvfDCCw2dFgAAAAAAAOC4Bm/GZWZm6tChQzp16pQ+//xzbd++vU7jM2fO1KlTp3Tq1CnNnDmzodMCAAAAAAAAHNfgzbg9e/ZoxIgRatmypUaMGKGPPvqoTuNlZWUqLS1t6HQAAAAAAACAoBFmjDEN+Qc+++yzKikp0dy5c/XUU0+pefPmmj17do3j4eHhSklJ0enTpzV8+HC98cYb6tChgyQpKytL2dnZfnEmTpzYkGkjBB3LK9T/rd7ncyyiXXPNnvh9hzJCMJi3aq9yvy7yOTZrQj91ac9zKL+r/rXriNJ3H/U5FjswUrcO6upQRgAAAAC+K3r06OF3rME/wKFdu3b64osvJEkFBQXq0qWLpPMf0lDd+EMPPaSZM2equLhYcXFxWrFihaZPny5Jio6OVnR0tE+MlJSUgJNpDDk5OVZi2YrjplhNck9L8m3GNWvWrNHn5pbvnxNxbMRq1uxTSb7NuG7duql7RNtGi+mm758TsRo7Tvucc5J8m3Ht27d3zVrhxppo7FjHTp1RyvLzj8koLi7WpZdeqi4dWmnmlGGNEs/LLd8/J+K4NZYb52QzlhvnZDOWG+dkM5Yb52QzlhvnZDOWG+dkM5btOQXS4M24wYMHa8mSJfriiy/09ttva8qUKZLON9Ak6dZbb/Ub936a6rlz53Ty5El973vfa+i0AAAAJEklpeX675G8KkfOqbi03LF8AAAA8N3S4M+Mu/766zVq1CiNGDFCo0aN0pAhQyRJLVq0UIsWLQKOr1q1Sv3799eQIUPUp08fTZo0qaHTAgAAAAAAABzX4FfGhYWF6bnnntNzzz3nc7zqJ6ReOB4fH6/4+PiGTgUAAAAAAAAIKg1+ZRwAAAAAAACAwGjGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgCc04AAAAAAAAwBKacQAAAAAAAIAlNOMAAAAAAAAAS2jGAQAAAAAAAJbQjAMAAAAAAAAsoRkHAAAAAAAAWEIzDgAAAAAAALCEZhwAAAAAAABgSROnEwAAAACclrh4k77MPS1JMsYoLGy3UqePUVTnNg5nBgAA3IZmHAAAAL7zikvKVFxa7nPMGONQNgAAwM24TRUAAAAAAACwhGYcAAAAAAAAYAnNOAAAAAAAAMASmnEAAAAAAACAJXyAAwAAAAAAtfjyeL4SXtggyfupy7sU1bmNXki4xeHMAIQamnEAAAAAANTCGKOy8oqqRy74PQDUTaPcprp//349//zz+vjjj+s8Xtt7AAAAAAAAgFDX4FfGeTwexcTEaPz48UpJSdHevXvVoUOHGseNMTW+BwAAAABsWrl5v5Zv3l/lyPuKu7mvJt/c17GcAASfGc+n61BufpUj72vxr2IV1bmNYzkh+DV4My49PV2xsbFavHixCgoKtHHjRk2ZMqXG8fLy8hrfAwAAAAA2VRgjY4zfMQCoqrzCf6248PfAhRq8GXfkyBF17dpVkhQVFaXDhw/XOl5RUVHjewAAAAAAAAA3aPBmXFhYmMLCwnx+X9t4Te/JyspSdna2z5/RtGlTpaSkNHTqCEHR7S44UCKlpOxxJBcEhyskXXFBXaz4f390JBcEjwvXii93HVTKrvXOJIOgwPkDF+L8gUA4f+BCnD9wIc4fqEmnTp3Uo0cP/wHTwF599VUzdepUY4wxP/nJT8yyZcuMMcZkZmaazMzMgOPVvac6ycnJDZ2247HcOCebsdw4J5ux3Dgnm7HcOCebsdw4J5ux3Dgnm7HcOCebsdw4J5ux3Dgnm7HcOCebsdw4J5ux3Dgnm7HcOCebsdw4J5uxgmFODf5pqrGxsUpPT9dDDz2kDRs2aMyYMZKkjIwMZWRkBByv7j0AAAAAAACAmzR4M65jx47KyMjQtddeq4yMDHXs2FGSFB0drejo6IDj1b0HAAAAAAAAcJMGf2acJPXt21d9+/p+5HdMTEyN44GOAQAAAAAAAG4SnpSUlOR0Eheje/furovlxjnZjOXGOdmM5cY52YzlxjnZjOXGOdmM5cY52YzlxjnZjOXGOdmM5cY52YzlxjnZjOXGOdmM5cY52YzlxjnZjOXGOdmM5fScwowxxloGAAAAAAAAwHdYgz8zDgAAAAAAAEBgIXubam327dunAwcOBLwccP/+/VqxYoXatGmjTp06OZDdN/Lz8/Xyyy/rq6++0rXXXhvwNevWrVN2drYGDBhgObuL9+abb2rLli265pprdOmll/qMbdmyRW+88Ybef/99RUVFqXXr1g5lWbuaauWLL77Qa6+9pi1btkiSoqKiHMiw/txac5L0+uuvq3PnzmrZsqXfWE01GcxqWsu81qxZI4/HY/VS62+jrKxMr7zyigYOHOg3dvjwYb388sv65JNP1KtXLzVp0iiPNm1Qta1pobTmedVlfTt79qzS0tJUWloaEutfYWGhVq1apbfeeksHDx7U97//fYWFhfm8pi7rY7DZsmWL/vGPf+jdd99Vz549ddlllwV8XUlJiZ5//nldffXVAdfIYJKTk6OVK1fqnXfeUdOmTdW1a1e/12RmZurvf/+7SkpKdNVVVzmQ5cX75JNP9Oabb/qsgYWFhVq9erXeeust/e9//1OvXr0UHh7uYJb1U1N9HThwQC+//LJ69+6tFi1aOJRh3WVlZWnFihXKzs5Wdna2JP/bi4JpL1EXHo9HL774YuWcPv3004DnYClwfQartLQ0bdq0qXJevXr18qm/0tJSLVu2TG+//bYiIyPVrl07B7Otu5rOr6G6/5Bq31+E2v6jtvqTQm//UZf1zytU9h91Wf+c2n+48sq49PR0TZgwQRkZGX5jHo9HMTExOnDggGJiYnTy5EkHMvxGfHy8MjIyNGvWLK1cudJvfNGiRXr66af19ddfO5DdxVm2bJlmz56tTZs26b777vMb/+CDD5Sbm6udO3dq6NChKi4udiDL2tVWK59//rkOHjyoo0eP6o477qg8KQY7N9acJM2dO1fx8fHKzc31G6utJoNVTWuZ14YNGzR58uQaXxNMcnNzNW7cOKWmpvqNFRUVadiwYdqzZ4/S0tI0ffp0BzKsv9rWtFBZ86qqbX2rqKjQLbfcou3bt+vcuXPOJFlP+fn52rNnj/Ly8rR48WI9/PDDfq+pbX0MRh988IGOHz+uDz/8UEOGDKn27yMhIUEzZ84MuEYGm5ycHB06dEi5ubmaMGGC0tPTfcY3b96syZMn6+jRo5o8ebI2bNjgUKb1d+rUqYBrYH5+vj766CPl5eVp4cKFSkxMdCjDi1Ndfe3fv1+xsbE6duyYSktLHcqufjIyMrR27Vrl5eUpLy9PRUVFPuPBtpeoi9zcXC1YsKByTvn5+QFfV119BqvU1FR99tlnlfMqLy/3GU9ISNCSJUv08ccf6/rrr1dhYaFDmdZdbefXUN1/1La/CMX9R35+fmXtLViwQKdOnfIZD8X9R1FRUeWc1q5dq23btgV8XSjtP8rLyyvn9Nlnn+mll17yGXd0/2FcaNOmTWb48OFmzpw5fmOvvvqqmTp1qjHGmB//+Mdm+fLllrP7xpkzZ0z79u1NWVmZ+ec//2nGjx/vM15eXm4iIyPN5DL0vAAADWtJREFU0aNHHcrw4owdO9asW7fOlJaWmvbt25tz585V+9quXbuanJwci9nVXX1q5Ve/+pWZP3++rdQumltrzhhjFi1aZDp27Gj27dvnN1afmgwmNa1lxhhz4MABM3jwYDNjxoxqXxNsjh07ZqZNm2b69u0bcCwiIsIUFxebzMxMM2bMGAcy/HZqW9OCec2rTqD1bevWrWbEiBEOZfTtbdu2zcTExPgcq219DHYVFRWme/fuJjc312/sD3/4g/nZz35m+vbtG3CNDGYJCQnmT3/6k8+xF1980TzwwAOV40uWLHEitXorLS01t9xyi1mwYEHANdArKyvLDBkyxGJm305N9TVjxgzzwgsvOJTZxZkzZ06N59Rg2kvU1b59+2qsOWOMKSsrM7fffrtJSUmp9bXBorY17aabbjIbN240xhgTFRVlPB6PrdQuWn3Or6Gy/6htfxHK+w9jjNm5c6cZOXKk3/FQ3X8YY0xJSYnp3bt3wP+z5uTkmMGDB5uHH344ZPYfXo8++qh58cUXfY45uf8I/vt/qpGVlVV56WRVw4cPV0xMjLKysgK+7+jRo5W3O0RFRenw4cONmqd0/idoaWlpfscLCgrUqVMnhYeHB8zF4/GouLhYGRkZOnv2rH7+85/73VLjpLS0NHk8Hr/je/bsUbdu3dSkSRN17NhRubm5uvLKK/1et2/fPrVq1UpXXHGFhWzrr661Ulpaqq1bt+rPf/6zzfQuyvHjx0O65mqSmJgY8N+ZJB05cqRONRlsalrLCgoKFB8fr1deeUWrV6+2nNnFi4iIUGJioiZNmhRwbPz48Ro6dKh69uyp+fPnO5DhxattTQv2NS+Q6ta3vXv3qnPnznruuef0gx/8QKNGjXIow/rxeDxasGCBdu7c6Ten2tbHYLZ48WKlp6drzpw56ty5s8/Ytm3btHr1av3rX/8KidvOvLZt26Zly5bp7Nmzmjp1qs9YXFychg0bpnvuuUfGGMXFxTmTZD09/vjjGj16tGJjY/XKK69U+7qNGzdq9OjRFjO7eLXV1549exQZGan58+fr3nvvVWRkpANZ1l92drbmz5+vkSNH6oYbbvAZc2Iv0RA8Ho9SUlLUvXt3TZgwQU2bNvUZf+yxxzRq1CjFxsbqr3/9q0NZ1l9aWpquvPJKTZw4UZdffrnP2Jw5czRhwgSNGzdOM2bMUIcOHRzKsu7qen4Npf1HbfuLUN5/SNITTzyhp59+2u94qO4/pPP/rkaPHu33GIiCggLFxcWF3P5DOn8r6vr16/Xhhx/6HHdy/xGyt6lWvYSy6q8LLyUPxPY/7qqXRlb9lZ+f75OLueCDbfPz81VUVKRdu3bptdde029+8xuredem6qW5VX9deIl4ICdPntTcuXO1Zs0aXXJJ8JZhXWrl0Ucf1ezZszVo0CALGX17oVxz30bVeYfSCb46L730ktq0aaP169dXPgOhusZdqKioqNC///1v/eUvf9GZM2e0fv16p1Oqs9rWtFBZ8y5U3fpWUFCgTz75RF999ZUefPBBvfPOOw5lWD/e89OZM2f8blOQal4fg1lJSYlat26tZ555xu826MTERPXv31+pqamVPxwM9IO0YFNSUqIWLVpo06ZN2rFjh8/Y559/rsGDB+uee+7R7t279emnnzqUZd199tlnWrlypcrKyir/DgL9ACk9PV0ej0dPPvmkA1nWX231VVBQoPfee085OTmKiYkJidv0o6OjNWjQIB05ckR33nmntm7d6veaUPt/RMeOHTV16lTl5eXp97//vX7961/7jNe1PoPNtGnT1KxZM+3YsUNDhw71uxV606ZNSk1N1VVXXaVVq1aprKzMoUzrrq7n11Daf9S2vwjl/cfmzZvVrFkz3XTTTQHHQ3H/UVhYqNTUVM2aNctvLJT3H7/73e/0+OOP+z27z8n9R8heGRcTE6OYmJg6v95bJJGRkdq8ebOk893qvn37Nkp+VUVERCg5Odnv+NmzZ7Vs2TKVl5fryJEjlT9l83g8evPNNzVlyhS1adNGqampeu+995SQkNDoudZHdc8z+c9//qMjR46oX79+8ng8lT+lT0tL09ixY1VSUqLJkydr6dKluuaaa2ymXC/V1Yq3loYNG6aEhAT17t1bEyZMcCzP+ujcubNOnDgRsjVXX96ai4yM1OHDh9W3b195PJ6QeNhydbz1N2TIEJ0+fVp5eXmVz0Cpyw8jgpG3/kaPHq3jx4/ruuuuU1JSkhISEjR79myn06uV97lVF65pobbmVVVRURFwfat6Lh01apRSUlJUUVGhXbt2hcTVcd7z8fbt2/XII49I+qb+Jk+eHHB9DAXe83FUVJSOHTumK664orL+7r33XuXm5lb+sCw/P79OPzRzmvf/eZdcconef/993XTTTZX19+677yoiIkK33XabNm/erM2bNwf9VX9t2rRRfHx85Q9jvX8X3vqbNm2a1q9frz/+8Y9as2ZNyHx4Q3X15a2/rl276pe//KVGjhypq666qrI+g1nVPUZ4eLhf/Tmxl/i2qu5Fxo4d67f+3XHHHQHrM9hV3YtERUXpq6++Uvfu3Svr7+2339add96p+Ph4LVmyRIcPHw76K5OqO7+G8v4jMjIy4P4i1Pcfxhg9+eSTfj/cC/X9x+LFizV+/Hh16dKl8lio7z/++9//Kjs7W4sXL648FhT7D2s3xFqUmZlpYmJiTExMjMnMzDTGfPP8hxMnTpguXbqYBx980HTp0sWcOHHC0VzHjh1rxo8fb/r06WOWLVtmjPF9rsO4cePM5MmTzYgRI8yTTz7pZKp19re//c306dPHjB8/3owdO7byuPe5DjfeeKOZMmWKSU5ONsnJyY7/HVSnulrx1tKiRYtMv379KufhrbVg58aaM8aYpUuXmoiICJOYmFj5d+WtuepqMtjVtJZVVdvzbYLJiRMnTGJioomIiDBLly41xnxTfyUlJaZnz55mypQpZtiwYeaJJ55wONu6qW5NC7U1r6rq1jdvrXk8HtO1a1eTmJhoIiMjze7dux3OuHYnTpwwycnJJikpyVx33XVm3rx5xhjf9S/Q+hjsli5daubNm2d+9KMfmYEDB5ry8nJjTOBnKYXKM+MyMzNNcnKyeeSRR0ynTp0qc/bW344dO0y7du1MYmKi6dKli9m1a5fDGddP1Zrzfp2Tk2Nat25tnnrqKZOcnFy5PoaSqvXl/Xr58uWmf//+5qc//anp3bu3KSsrczjL2nnr79FHHzWdOnUye/fuNcYE716iLi5c/5599lljTOBnydXl+XLBour6N2DAAL/177HHHjMDBgww999/f8jUX3Xn11DffwTaX4T6/mPNmjXm7rvv9jseyvuPgoICc/XVV5uTJ0/6HA/1/cc999xjXnvtNZ9jwbD/CE9KSkqy0/az58CBAyoqKlJkZKS6d++uHj16qKysTN27d1e/fv106623Kj8/X0lJSY7/dOS2227T2bNnNW7cOE2cOFHS+S5706ZNdeONN+qOO+7Q6dOnNXLkSE2fPj0kLm+97rrr1K1bN3Xq1Elz5sypvBS0uLhYQ4cOVUVFhZo0aaKioiIVFRVp6NChatWqlcNZ+2vZsmXAWvHWUkREhM88vLUW7NxYc5K0detWXX311QoPD6+sKW/N3XjjjQFrMtjVtJZVrbVAx4KV95al/v37V9act/6GDx+uSZMm6fTp07r55ptDpv7y8/MDrmmhtuZVdfbs2YDr24Xn0hMnTujxxx8PidtkwsLC9OWXX6qwsFCTJk3StGnTJPmuf4HWx2D39ddf6/jx4+rVq5cWLFig5s2bS/rmnFu11gIdC0ZlZWU6dOiQLrvsMj3zzDOVVx5562/kyJEaNWqUTp8+HTK3aVVVtea8Xw8cOFDl5eUqLy9XUVFR5XgoqVpf3q9vuOEGdevWTZdeeqkWLlwY9LUnnb9F+uDBg2rVqpXmzZunPn36SFLQ7iXq6tChQyouLlZcXJzuv/9+Sb616BXoWLA6deqUjh8/rj59+mjhwoV+699dd92ltm3bqm3btlq0aFFI1J93/3Hh+TXU9x+B9hehvv/YuXOn7rvvPr9nEYby/mPv3r0aMmSI39Xmobz/KCoq0oEDB/SLX/zC73EkTu8/wowJoYeiAAAAAAAAACEsdJ4iDQAAAAAAAIQ4mnEAAAAAAACAJTTjAAAAAAAAAEtoxgEAAAAAAACW0IwDAAAAAAAALKEZBwAAAAAAAFhCMw4AAAAAAACwpInTCQAAAMAZWVlZys7O1vDhw1VWVqbdu3fr+uuvV3R0tNOpAQAAuBbNOAAAgO+ojIwMzZ07V4MHD9bIkSO1fPly5ebmavv27brhhhucTg8AAMCVuE0VAADgO+7222/XwoULFRcXJ2OMtm7d6nRKAAAArkUzDgAAAJKk1q1bS5IKCwsdzgQAAMC9aMYBAAAAAAAAltCMAwAAAAAAACwJT0pKSnI6CQAAANhXVlamyMhI/fCHP1SPHj38fg8AAICGF2aMMU4nAQAAAAAAAHwXcJsqAAAAAAAAYAnNOAAAAAAAAMASmnEAAAAAAACAJTTjAAAAAAAAAEtoxgEAAAAAAACW/H+7Mr+V7G/h2QAAAABJRU5ErkJggg==",
      "image/svg+xml": [
       "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n",
       "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n",
       "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" class=\"marks\" width=\"1251\" height=\"664\" viewBox=\"0 0 1251 664\"><rect width=\"1251\" height=\"664\" fill=\"white\"/><g fill=\"none\" stroke-miterlimit=\"10\" transform=\"translate(45,27)\"><g class=\"mark-group role-frame root\" role=\"graphics-object\" aria-roledescription=\"group mark container\"><g transform=\"translate(0,0)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0.5,0.5h1200v600h-1200Z\" stroke=\"#ddd\"/><g><g class=\"mark-group role-axis\" aria-hidden=\"true\"><g transform=\"translate(0.5,600.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-grid\" pointer-events=\"none\"><line transform=\"translate(0,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(27,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(53,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(80,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(107,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(133,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(160,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(187,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(213,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(240,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(267,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(293,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(320,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(347,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(373,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(400,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(427,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(453,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(480,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(507,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(533,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(560,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(587,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(613,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(640,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(667,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(693,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(720,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(747,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(773,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(800,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(827,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(853,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(880,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(907,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(933,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(960,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(987,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1013,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1040,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1067,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1093,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1120,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1147,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1173,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1200,-600)\" x2=\"0\" y2=\"600\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-group role-axis\" aria-hidden=\"true\"><g transform=\"translate(0.5,0.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-grid\" pointer-events=\"none\"><line transform=\"translate(0,600)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,545)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,491)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,436)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,382)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,327)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,273)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,218)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,164)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,109)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,55)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,0)\" x2=\"1200\" y2=\"0\" stroke=\"#ddd\" stroke-width=\"1\" opacity=\"1\"/></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-group role-axis\" role=\"graphics-symbol\" aria-roledescription=\"axis\" aria-label=\"X-axis titled 'n' for a linear scale with values from −1 to 8\"><g transform=\"translate(0.5,600.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-tick\" pointer-events=\"none\"><line transform=\"translate(0,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(27,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(53,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(80,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(107,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(133,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(160,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(187,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(213,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(240,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(267,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(293,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(320,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(347,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(373,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(400,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(427,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(453,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(480,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(507,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(533,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(560,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(587,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(613,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(640,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(667,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(693,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(720,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(747,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(773,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(800,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(827,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(853,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(880,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(907,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(933,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(960,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(987,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1013,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1040,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1067,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1093,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1120,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1147,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1173,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(1200,0)\" x2=\"0\" y2=\"5\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g><g class=\"mark-text role-axis-label\" pointer-events=\"none\"><text text-anchor=\"start\" transform=\"translate(0,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">−1.0</text><text text-anchor=\"middle\" transform=\"translate(26.66666666666666,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">−0.8</text><text text-anchor=\"middle\" transform=\"translate(53.333333333333336,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">−0.6</text><text text-anchor=\"middle\" transform=\"translate(80,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">−0.4</text><text text-anchor=\"middle\" transform=\"translate(106.66666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">−0.2</text><text text-anchor=\"middle\" transform=\"translate(133.33333333333331,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">0.0</text><text text-anchor=\"middle\" transform=\"translate(160,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.2</text><text text-anchor=\"middle\" transform=\"translate(186.66666666666666,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">0.4</text><text text-anchor=\"middle\" transform=\"translate(213.33333333333334,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.6</text><text text-anchor=\"middle\" transform=\"translate(240,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">0.8</text><text text-anchor=\"middle\" transform=\"translate(266.66666666666663,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">1.0</text><text text-anchor=\"middle\" transform=\"translate(293.33333333333337,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">1.2</text><text text-anchor=\"middle\" transform=\"translate(320,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">1.4</text><text text-anchor=\"middle\" transform=\"translate(346.6666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">1.6</text><text text-anchor=\"middle\" transform=\"translate(373.3333333333333,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">1.8</text><text text-anchor=\"middle\" transform=\"translate(400,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">2.0</text><text text-anchor=\"middle\" transform=\"translate(426.6666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">2.2</text><text text-anchor=\"middle\" transform=\"translate(453.3333333333333,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">2.4</text><text text-anchor=\"middle\" transform=\"translate(480,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">2.6</text><text text-anchor=\"middle\" transform=\"translate(506.6666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">2.8</text><text text-anchor=\"middle\" transform=\"translate(533.3333333333333,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">3.0</text><text text-anchor=\"middle\" transform=\"translate(560,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">3.2</text><text text-anchor=\"middle\" transform=\"translate(586.6666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">3.4</text><text text-anchor=\"middle\" transform=\"translate(613.3333333333333,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">3.6</text><text text-anchor=\"middle\" transform=\"translate(640,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">3.8</text><text text-anchor=\"middle\" transform=\"translate(666.6666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">4.0</text><text text-anchor=\"middle\" transform=\"translate(693.3333333333334,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">4.2</text><text text-anchor=\"middle\" transform=\"translate(720.0000000000001,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">4.4</text><text text-anchor=\"middle\" transform=\"translate(746.6666666666666,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">4.6</text><text text-anchor=\"middle\" transform=\"translate(773.3333333333333,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">4.8</text><text text-anchor=\"middle\" transform=\"translate(800,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">5.0</text><text text-anchor=\"middle\" transform=\"translate(826.6666666666666,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">5.2</text><text text-anchor=\"middle\" transform=\"translate(853.3333333333334,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">5.4</text><text text-anchor=\"middle\" transform=\"translate(879.9999999999999,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">5.6</text><text text-anchor=\"middle\" transform=\"translate(906.6666666666666,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">5.8</text><text text-anchor=\"middle\" transform=\"translate(933.3333333333334,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">6.0</text><text text-anchor=\"middle\" transform=\"translate(960,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">6.2</text><text text-anchor=\"middle\" transform=\"translate(986.6666666666667,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">6.4</text><text text-anchor=\"middle\" transform=\"translate(1013.3333333333334,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">6.6</text><text text-anchor=\"middle\" transform=\"translate(1040,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">6.8</text><text text-anchor=\"middle\" transform=\"translate(1066.6666666666665,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">7.0</text><text text-anchor=\"middle\" transform=\"translate(1093.3333333333333,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">7.2</text><text text-anchor=\"middle\" transform=\"translate(1120,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">7.4</text><text text-anchor=\"middle\" transform=\"translate(1146.6666666666665,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">7.6</text><text text-anchor=\"middle\" transform=\"translate(1173.3333333333335,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">7.8</text><text text-anchor=\"end\" transform=\"translate(1200,15)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"0\">8.0</text></g><g class=\"mark-rule role-axis-domain\" pointer-events=\"none\"><line transform=\"translate(0,0)\" x2=\"1200\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g><g class=\"mark-text role-axis-title\" pointer-events=\"none\"><text text-anchor=\"middle\" transform=\"translate(600,30)\" font-family=\"sans-serif\" font-size=\"11px\" font-weight=\"bold\" fill=\"#000\" opacity=\"1\">n</text></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-group role-axis\" role=\"graphics-symbol\" aria-roledescription=\"axis\" aria-label=\"Y-axis titled 'nrow' for a linear scale with values from 0.0 to 0.6\"><g transform=\"translate(0.5,0.5)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-rule role-axis-tick\" pointer-events=\"none\"><line transform=\"translate(0,600)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,545)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,491)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,436)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,382)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,327)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,273)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,218)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,164)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,109)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,55)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/><line transform=\"translate(0,0)\" x2=\"-5\" y2=\"0\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g><g class=\"mark-text role-axis-label\" pointer-events=\"none\"><text text-anchor=\"end\" transform=\"translate(-7,603)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.00</text><text text-anchor=\"end\" transform=\"translate(-7,548.4545454545454)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.05</text><text text-anchor=\"end\" transform=\"translate(-7,493.9090909090909)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.10</text><text text-anchor=\"end\" transform=\"translate(-7,439.3636363636364)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.15</text><text text-anchor=\"end\" transform=\"translate(-7,384.8181818181818)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.20</text><text text-anchor=\"end\" transform=\"translate(-7,330.27272727272725)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.25</text><text text-anchor=\"end\" transform=\"translate(-7,275.72727272727275)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.30</text><text text-anchor=\"end\" transform=\"translate(-7,221.18181818181824)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.35</text><text text-anchor=\"end\" transform=\"translate(-7,166.63636363636363)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.40</text><text text-anchor=\"end\" transform=\"translate(-7,112.09090909090912)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.45</text><text text-anchor=\"end\" transform=\"translate(-7,57.54545454545456)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.50</text><text text-anchor=\"end\" transform=\"translate(-7,3)\" font-family=\"sans-serif\" font-size=\"10px\" fill=\"#000\" opacity=\"1\">0.55</text></g><g class=\"mark-rule role-axis-domain\" pointer-events=\"none\"><line transform=\"translate(0,600)\" x2=\"0\" y2=\"-600\" stroke=\"#888\" stroke-width=\"1\" opacity=\"1\"/></g><g class=\"mark-text role-axis-title\" pointer-events=\"none\"><text text-anchor=\"middle\" transform=\"translate(-29,300) rotate(-90) translate(0,-2)\" font-family=\"sans-serif\" font-size=\"11px\" font-weight=\"bold\" fill=\"#000\" opacity=\"1\">nrow</text></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g><g class=\"mark-rect role-mark marks\" role=\"graphics-object\" aria-roledescription=\"rect mark container\"><path aria-label=\"n: 0; nrow: 0.501369863014\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M130.83333333333331,53.051058530510595h5v546.9489414694895h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 1; nrow: 0.282191780822\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M264.16666666666663,292.1544209215443h5v307.8455790784557h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 2; nrow: 0.145205479452\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M397.5,441.59402241594023h5v158.40597758405977h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 3; nrow: 0.0493150684932\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M530.8333333333333,546.2017434620175h5v53.798256537982525h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 4; nrow: 0.0109589041096\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M664.1666666666667,588.0448318804483h5v11.955168119551672h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 5; nrow: 0.0027397260274\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M797.5,597.0112079701121h5v2.988792029887918h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 6; nrow: 0.00547945205479\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M930.8333333333334,594.0224159402242h5v5.977584059775836h-5Z\" fill=\"#4c78a8\"/><path aria-label=\"n: 7; nrow: 0.0027397260274\" role=\"graphics-symbol\" aria-roledescription=\"bar\" d=\"M1064.1666666666665,597.0112079701121h5v2.988792029887918h-5Z\" fill=\"#4c78a8\"/></g><g class=\"mark-group role-title\"><g transform=\"translate(600,-22)\"><path class=\"background\" aria-hidden=\"true\" d=\"M0,0h0v0h0Z\" pointer-events=\"none\"/><g><g class=\"mark-text role-title-text\" role=\"graphics-symbol\" aria-roledescription=\"title\" aria-label=\"Title text 'Poisson-styled reprezentation of data'\" pointer-events=\"none\"><text text-anchor=\"middle\" transform=\"translate(0,10)\" font-family=\"sans-serif\" font-size=\"13px\" font-weight=\"bold\" fill=\"#000\" opacity=\"1\">Poisson-styled reprezentation of data</text></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" pointer-events=\"none\" display=\"none\"/></g></g></g><path class=\"foreground\" aria-hidden=\"true\" d=\"\" display=\"none\"/></g></g></g></svg>\n"
      ],
      "text/plain": [
       "@vlplot(\n",
       "    height=600,\n",
       "    width=1200,\n",
       "    title=\"Poisson-styled reprezentation of data\",\n",
       "    mark=\"bar\",\n",
       "    encoding={\n",
       "        x={\n",
       "            field=\"n\"\n",
       "        },\n",
       "        y={\n",
       "            field=\"nrow\"\n",
       "        }\n",
       "    },\n",
       "    data={\n",
       "        values=...\n",
       "    }\n",
       ")"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mod |> @vlplot(\n",
    "    height=600,\n",
    "    width=1200,\n",
    "    :bar,\n",
    "    x=:n,\n",
    "    y=:nrow,\n",
    "    title = \"Poisson-styled reprezentation of data\"\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57df78c7-1934-46b2-ad01-e9fccdfafdcd",
   "metadata": {},
   "source": [
    "> Tu pojawi się dopasowanie rozkładu Poissona i model predykcji"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7eabef55-1a09-4c94-99cd-4f4401e20b02",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Julia 1.7.2",
   "language": "julia",
   "name": "julia-1.7"
  },
  "language_info": {
   "file_extension": ".jl",
   "mimetype": "application/julia",
   "name": "julia",
   "version": "1.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
