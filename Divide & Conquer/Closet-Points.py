from math import inf

def squared_euclidean_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def sort_by_column(arr, col=0):
    return sorted(arr, key=lambda item: item[col])

def min_distance_among_pairs(pts, count, min_dist=inf):
    for i in range(count - 1):
        for j in range(i + 1, count):
            min_dist = min(min_dist, squared_euclidean_distance(pts[i], pts[j]))
    return min_dist

def min_distance_in_strip(pts, count, min_dist=inf):
    for i in range(min(6, count - 1), count):
        for j in range(max(0, i - 6), i):
            min_dist = min(min_dist, squared_euclidean_distance(pts[i], pts[j]))
    return min_dist

def closest_pair_squared(pts_x_sorted, pts_y_sorted, count):
    if count <= 3:
        return min_distance_among_pairs(pts_x_sorted, count)
    
    mid_idx = count // 2
    left_closest = closest_pair_squared(pts_x_sorted, pts_y_sorted[:mid_idx], mid_idx)
    right_closest = closest_pair_squared(pts_y_sorted, pts_y_sorted[mid_idx:], count - mid_idx)
    min_pair_distance = min(left_closest, right_closest)
    
    strip = [p for p in pts_x_sorted if abs(p[0] - pts_x_sorted[mid_idx][0]) < min_pair_distance]
    
    return min(min_pair_distance, min_distance_in_strip(strip, len(strip), min_pair_distance))

def closest_pair(pts, count):
    sorted_x = sort_by_column(pts, col=0)
    sorted_y = sort_by_column(pts, col=1)
    return closest_pair_squared(sorted_x, sorted_y, count) ** 0.5

if __name__ == "__main__":
    sample_points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Distance:", closest_pair(sample_points, len(sample_points)))
