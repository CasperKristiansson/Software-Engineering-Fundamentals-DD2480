import itertools
import math

def _determine_quadrant(point: tuple[float, float] | list[float]) -> int:
    """Check what quadrant a point lies in, favouring lower numbered quadrants. Utility funciton.

    :param point: The point to check quadrant for.
    :type point: tuple[float, float] | list[float]

    :return: Returns the quadrant encoded as an integer in the range [1, 4]
    :rtype: int
    """
    x, y = point

    if x >= 0 and y >= 0:
        return 1
    elif x <= 0 and y >= 0:
        return 2
    elif x <= 0 and y <= 0:
        return 3
    else:
        return 4

def _check_tripoint_radius(
        a: tuple[float, float] | list[float],
        b: tuple[float, float] | list[float],
        c: tuple[float, float] | list[float],
        r: float) -> bool:
    """Check that a, b, and c can be contained on/within
    a circle of radius at most r.

    Uses all points to calculate a different centroids
    points and checks that all points are accessible
    from the centroid with at most r radius.

    :param a: First point.
    :type a: tuple[float, float] | list[float]

    :param b: Second point.
    :type b: tuple[float, float] | list[float]

    :param c: Third point.
    :type c: tuple[float, float] | list[float]

    :return: Returns wether or not all three points can
    be contained or on a circle of radius r.
    :rtype: bool
    """

    # Centroid combinations of 2 points
    for p1, p2 in itertools.combinations([a, b, c], 2):
        centroid = (p1[0] + p2[0]) / 2, \
                    (p1[1] + p2[1]) / 2

        if math.dist(centroid, a) <= r and \
                math.dist(centroid, b) <= r and \
                math.dist(centroid, c) <= r:
            return True
    
    # Final centroid, between all three points
    centroid = (a[0] + b[0] + c[0]) / 3, \
                (a[1] + b[1] + c[1]) / 3

    return math.dist(centroid, a) <= r and \
            math.dist(centroid, b) <= r and \
            math.dist(centroid, c) <= r

class CMV:
    def __init__(self, d):
        for k,v in d.items():
            setattr(self, k, v)
        self.CMV_VECTOR = self.construct_vector()
    
    def construct_vector(self):
        return [
            self.condition0(),
            self.condition1(),
            self.condition2(),
            self.condition3(),
            self.condition4(),
            self.condition5(),
            self.condition6(),
            self.condition7(),
            self.condition8(),
            self.condition9(),
            self.condition10(),
            self.condition11(),
            self.condition12(),
            self.condition13(),
            self.condition14(),
        ]
    
    def condition0(self):
        pass

    def condition1(self):
        pass

    def condition2(self):
        pass

    def condition3(self):
        """
        Determine whether there exists at least one set of three consecutive data points
        that are the vertices of a triangle with an area greater than the input parameter 
        AREA1.

        Parameters:
        - self: the CMV object

        Returns:
        - True if there exist a set of three consecutive data points with an area greater than AREA1
        - False otherwise
        """

        if len(self.POINTS) < 3:
            return False
        
        for i in range(len(self.POINTS)-2):
            (x1,y1) = self.POINTS[i]
            (x2,y2) = self.POINTS[i+1]
            (x3,y3) = self.POINTS[i+2]
            area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
            
            if area > self.AREA1:
                return True
        return False


    def condition4(self):
        """Check if `Q_PTS` sequential points lie in more quadrants than `QUADS`.

        Checks the condition by mapping each point of a sliding window to their
        respective quadrants and creating a set of these. The length of the set
        is compared to `QUADS` field to determine if the condition is upheld.

        Defaults to false if `Q_PTS < QUADS || NUMPOINTS < QUADS`.
        """

        if self.Q_PTS < self.QUADS or self.NUMPOINTS < self.QUADS:
            return False
        
        for i in range(0, self.NUMPOINTS - self.Q_PTS):
            window = self.POINTS[i : i + self.Q_PTS]
            quad_set = set(map(_determine_quadrant, window))
            if len(quad_set) > self.QUADS:
                return True
        return False

    def condition5(self):
        for i in range(0, self.NUMPOINTS - 1):
            x1, _ = self.POINTS[i]
            x2, _ = self.POINTS[i + 1]

            if x2 < x1:
                return True
        return False

    def condition6(self):
        """
        Determine whether there exists at least one set of N_PTS consecutive data points
        where at least one of the points (p_0) is a distance greater than DIST from the line between
        the first (p_1) and the last (p_2) of the N_PTS. If p_1 and p_2 coincide, then determine whether any
        of the other N_PTS is a distance greater than DIST from p_1 (the coincident point)

        Parameters:
        - self: the CMV object

        Returns:
        - True if any of the described criteria is fulfilled
        - False otherwise
        """

        if self.NUMPOINTS < 3:
            return False

        for i in range(len(self.POINTS)-self.N_PTS+1):
            n_points_array = self.POINTS[i:i+self.N_PTS]
            p_1 = n_points_array[0]
            p_2 = n_points_array[-1]
            if p_1 != p_2:
                for point_index in range(1, len(n_points_array)-1):
                    p_0 = n_points_array[point_index]
                    x_0, y_0 = p_0[0], p_0[1]
                    x_1, y_1 = p_1[0], p_1[1]
                    x_2, y_2 = p_2[0], p_2[1]  
                    distance_to_line = abs((x_2 - x_1)*(y_1 - y_0) - (x_1 - x_0)*(y_2 - y_1)) \
                                        / math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))

                    if distance_to_line > self.DIST:                        
                        return True
            else:
                for point_index in range(1, len(n_points_array)-1):
                    p_0 = n_points_array[point_index]
                    x_0, y_0 = p_0[0], p_0[1]
                    x_1, y_1 = p_1[0], p_1[1]
                    distance_to_point = math.sqrt(math.pow(x_1 - x_0,2) + math.pow(y_1 - y_0, 2))
                    if distance_to_point > self.DIST:
                        return True
        
        return False



    def condition7(self):
        """
        Determine whether there exists at least one set of data 
        points, separated by exactly K_PTS points, with a distance 
        greater than LENGTH1.

        Parameters:
        - self: the CMV object
        
        Returns:
        - True if the is a distance greater than LENGTH1
        - False otherwise
        """
        if self.NUMPOINTS < 3:
            return False
        for i in range(self.NUMPOINTS-self.K_PTS - 1):
            (x1,y1) = self.POINTS[i]
            (x2,y2) = self.POINTS[i + self.K_PTS + 1]

            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if dist > self.LENGTH1:
                return True
        return False

    def condition8(self):
        """Checks if three seperated points can be contained on/within a circle
        of radius at most `RADIUS1`.

        Uses a sliding window accross all points, where each window contains
        three points seperated by `A_PTS` and `B_PTS`. These points are then
        verified to be contained on  or within a circle of radius at most
        `RADIUS1` using the points centroid.

        Defaults to false if `NUMPOINTS < 5`.
        """
        # Spec condition
        if self.NUMPOINTS < 5:
            return False

        # -2 for offsetting three points, A_PTS and B_PTS for the seperation
        for i in range(0, self.NUMPOINTS - 2 - self.A_PTS - self.B_PTS):
            a = self.POINTS[i]
            b = self.POINTS[i + self.A_PTS + 1]
            c = self.POINTS[i + self.A_PTS + 1 + self.B_PTS + 1]

            if not _check_tripoint_radius(a, b, c, self.RADIUS1):
                return True

        return False

    def condition9(self):
        """
        Determine whether there exists at least one set of three points separated by C_PTS and D_PTS 
        consecutive intervening points that form an angle such that the internal angle is less than 
        pi - EPSILON or external angle is larger than pi + EPSILON. This is only possible if the first
        and third points do not coincide with the second point.

        Parameters:
        - self: the CMV object

        Returns:
        - True if any of the described criteria is fulfilled
        - False otherwise
        """

        if self.NUMPOINTS < 5:
            return False
        
        for i in range(self.NUMPOINTS - self.C_PTS - self.D_PTS - 2):
            (x1,y1) = self.POINTS[i]
            (x2,y2) = self.POINTS[i + self.C_PTS + 1]
            (x3,y3) = self.POINTS[i + self.C_PTS + self.D_PTS + 2]

            if ((x2,y2) not in [(x1,y1), (x3,y3)]):
                a = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))
                b = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
                c = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
                internal_angle = math.acos((math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / (2*a*b))
                external_angle = 2*math.pi - internal_angle
                if (internal_angle < math.pi - self.EPSILON) or (external_angle > math.pi + self.EPSILON):
                    return True

        return False
        

    def condition10(self):
        pass

    def condition11(self):
        """
        Determine whether there is at least one set of two data points, (X[i], Y[i]) and (X[j], Y[j]), separated by exactly G_PTS
        consecutive intervening points such that X[j] - X[i] < 0. (where i < j ) The condition is not met when NUMPOINTS < 3.

        Parameters:
        - self: the CMV object

        Returns:
        - True if X[j] - X[i] < 0 and NUMPOINTS > 2
        - False otherwise
        """
        if self.NUMPOINTS < 3:
            return False
        for i in range(self.NUMPOINTS - self.G_PTS - 1):
            (xi, _) = self.POINTS[i]
            (xj, _) = self.POINTS[i + self.G_PTS + 1]

            if xj - xi < 0:
                return True
        return False

    def condition12(self):
        pass

    def condition13(self):
        pass

    def condition14(self):
        pass
