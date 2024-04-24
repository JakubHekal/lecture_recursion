import matplotlib.pyplot as plt


def flood_fill(img, x, y):
    if 0 <= y < len(img) and 0 <= x < len(img[0]):
        v = int(img[y, x])
        if v == 1:
            img[y, x] = 2

            plt.imshow(img, cmap='gray')
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()

            img = flood_fill(img, x + 1, y)
            img = flood_fill(img, x - 1, y)
            img = flood_fill(img, x, y + 1)
            img = flood_fill(img, x, y - 1)

    return img


def main():

    for i in range(3):
        img = plt.imread(f"files/img{i}.png")[:, :, 0]

        img = flood_fill(img, 0, 0)

        plt.imshow(img, cmap='gray')
        plt.show()


if __name__ == "__main__":
    main()
