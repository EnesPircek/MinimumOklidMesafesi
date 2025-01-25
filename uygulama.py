import math

def euclideanDistance(point1, point2): # 2 nokta arasındaki öklid mesafesini hesaplayan fonksiyonu tanımladım.

	return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 2D uzayındaki noktaları tanımlayalım
points = [(2, 3), (5, 8), (1, 1), (7, 6)]

# Tüm mesafeleri saklayacağımız bir liste
distances []

# Her nokta çifti arasındaki mesafeyi hesaplayalım
for i in range(len(points)):
	for j in range(i + 1, len(points)):
		distance = euclideanDistance(points[i], points[j])
		distances.append((points[i], points[j], distance))

# minimum mesafeyi bulalım
min_distance = min(distances, key=lambda x: x[2])

# Sonuçları yazdıralım
print("Tum mesafeler:")
for p1, p2, dist in distances:
	print(f"{p1} ve {p2} arasındaki mesafe: {dist:.2f}")


print("\nEn kısa mesafe:")
print(f"{min_distance[0]} ve {min_distance[1]} arasındaki mesafe: {min_distance[2]:.2f}")