def create_bmi_app():
    class BMI:
        def __init__(self, weight, height):
            self.weight = weight
            self.height = height

        def calculate_bmi(self):
            return self.weight / (self.height ** 2)

        def get_category(self):
            bmi = self.calculate_bmi()
            if bmi < 0.00185:
                return "Underweight"
            elif 0.00185 <= bmi < 0.0025:
                return "Normal Weight"
            elif 0.0025 <= bmi < 0.0030:
                return "Overweight"
            else:
                return "Obese"

    def input_data():
        weight = float(input("Masukkan berat badan (kg): "))
        height = float(input("Masukkan tinggi badan (m): "))
        return weight, height

    def calculate_bmi():
        weight, height = input_data()
        bmi = BMI(weight, height)
        return bmi.calculate_bmi(), bmi.get_category()

    return calculate_bmi



bmi_app = create_bmi_app()


result, category = bmi_app()
print("BMI Anda adalah:", result)
print("Kategori BMI Anda:", category)
12