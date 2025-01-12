import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.
    :param point1: İlk nokta (x1, y1)
    :param point2: İkinci nokta (x2, y2)
    :return: İki nokta arasındaki mesafe
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# 2D uzayda noktalar
points = [(1, 2), (4, 6), (7, 8)]  # Noktaların (x, y) koordinatları

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktayı tekrar hesaplamamak için
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucun yazdırılması
print("Minimum Öklid Mesafesi:", min_distance)
