ax=sns.countplot(x="bedrooms", data=df, hue="basement", color='r')
#
# Добавление значений к каждому столбику
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'center',
                xytext = (0, 9),
                textcoords = 'offset points')
plt.show()