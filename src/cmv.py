import math

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
        pass

    def condition4(self):
        pass

    def condition5(self):
        pass

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
        pass

    def condition9(self):
        pass

    def condition10(self):
        pass

    def condition11(self):
        pass

    def condition12(self):
        pass

    def condition13(self):
        pass

    def condition14(self):
        pass