    
class Mandelbrot(object):

    @staticmethod
    def isInMandelbrotSet(x, y, iters, bounds):
        real = x
        imaginary = y
        for iteration in range(iters):
            temp_real = real * real - imaginary * imaginary + x
            temp_imaginary = 2 * real * imaginary + y

            real = temp_real
            imaginary = temp_imaginary

            if (abs(real * imaginary) > bounds):
                return [real, imaginary, iteration]
        return None

    @staticmethod
    def generate(width, height, iters, zoom, bounds, camx, camy):
        """
        Generates two sets of entries in JSON format.
        Set1: The set of canvas coordinates with the iteration required to prove as valid mandelbrot number (Number is not included).
        Set2: The set of canvas coordinates that result in NOT being a mandelbrot number.
        Neither set actually includes the mandelbrot number as that is not particularly important.
        Set 1 will be labeled as in, Set 2 will be labeled as out.
        Each entry to these sets will have a counter of the entries to that set as the entry's key.
        """

        set = [[],[]]
        max_iteration_reached = 0

        for x in range(width):
            for y in range(height):
                mag_x = x / zoom - camx
                mag_y = y / zoom - camy

                # returns [real, imaginary, iteration] for the given parameters
                result = Mandelbrot.isInMandelbrotSet(mag_x, mag_y, iters, bounds)

                # The current magnified x and y positions is not a mandelbrot number
                if (result == None):
                    set[1].append([x, y, 0])
                    continue

                # result -> [real, imaginary, iteration]
                iteration = result[2]
                # The current magnified x and y positions is not a mandelbrot number
                set[0].append([x, y, iteration])

                if (max_iteration_reached < iteration):
                    max_iteration_reached = iteration
                continue

            continue

        return [set, max_iteration_reached]



    # @staticmethod
    # def generate(width, height, iters, zoom, bounds, camx, camy):
    #     """
    #     Generates two sets of entries in JSON format.
    #     Set1: The set of canvas coordinates with the iteration required to prove as valid mandelbrot number (Number is not included).
    #     Set2: The set of canvas coordinates that result in NOT being a mandelbrot number.
    #     Neither set actually includes the mandelbrot number as that is not particularly important.
    #     Set 1 will be labeled as in, Set 2 will be labeled as out.
    #     Each entry to these sets will have a counter of the entries to that set as the entry's key.
    #     """
    #     # An id is required foin and out id are required to act as keys for each set submission
    #     id1 = 0
    #     id2 = 0

    #     set = {'in': {}, 'out': {}}

    #     for x in range(width):
    #         for y in range(height):
    #             mag_x = x / zoom - camx
    #             mag_y = y / zoom - camy

    #             result = Mandelbrot.isInMandelbrotSet(mag_x, mag_y, iters, bounds)

    #             # The current magnified x and y positions is not a mandelbrot number
    #             if (result == None):
    #                 set['out'][id2] = {'x':x, 'y':y}
    #                 id2 += 1
    #                 continue

    #             # result -> [real, imaginary, iteration]
    #             # The current magnified x and y positions is not a mandelbrot number
    #             set['in'][id1] = {'x': x, 'y': y, 'i': result[2]}
    #             id1 += 1

    #             continue
    #         continue

    #     return set




class Serpenski: pass