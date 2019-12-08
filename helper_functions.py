def plot_histkde(data, columns):
    for column in columns:
        sns.distplot(data[column], label=column)
        stat, p = shapiro(data[column])
        plt.title (column + ' Distribution')
        plt.legend()
        plt.show()
        print('Shapiro-Wilk Test Statistics=%.3f, p=%.3f' % (stat, p))
        alpha = 0.05
        if p > alpha:
            print('Sample looks Gaussian (fail to reject H0)')
        else:
            print('Sample does not look Gaussian (reject H0)')