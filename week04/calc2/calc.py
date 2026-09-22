class Calculator:
    def __init__(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _format_value(self, val):
        try:
            res = f"{round(val, 10):.10f}"
            if "." in res:
                res = res.rstrip('0').rstrip('.')
            if res == "-0":
                res = "0"
            return res if res != "" else "0"
        except Exception:
            return "0"

    def press(self, key: str) -> str:
        if self.is_error:
            if key == "C":
                self._reset()
                return self.display
            return self.display

        if key == "C":
            self._reset()
        elif key == "BS":
            self._handle_bs()
        elif key == "+/-":
            self._handle_plus_minus()
        elif key == "%":
            self._handle_percent()
        elif key in "0123456789.":
            self._handle_digit(key)
        elif key in "+-*/=":
            self._handle_operator(key)

        return self.display

    def _reset(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _handle_digit(self, key):
        if self.after_equals:
            self.current_num = ""
            self.running_total = 0.0
            self.last_operator = None
            self.after_equals = False
            self.is_typing = False
            self.has_decimal = False

        if key == ".":
            if not self.has_decimal:
                if self.current_num == "" or self.current_num == "0":
                    self.current_num = "0."
                else:
                    self.current_num += "."
                self.has_decimal = True
            return

        clean_num = self.current_num.replace(".", "").replace("-", "")
        if len(clean_num) < 12:
            if self.current_num == "0":
                self.current_num = key
            else:
                self.current_num += key
            self.is_typing = True

        if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
            self.current_num = self.current_num.lstrip("0")
            if self.current_num == "" or self.current_num.startswith("."):
                self.current_num = "0" + self.current_num

        self.display = self.current_num
        self.has_decimal = "." in self.current_num

    def _handle_bs(self):
        if self.after_equals:
            return

        if len(self.current_num) <= 1:
            self.current_num = "0"
            self.has_decimal = False
        else:
            self.current_num = self.current_num[:-1]
            if self.current_num == "" or self.current_num == "-":
                self.current_num = "0"
            if self.current_num.endswith("."):
                self.current_num = self.current_num[:-1]
                self.has_decimal = False
            
            if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
                self.current_num = self.current_num.lstrip("0")
                if self.current_num == "" or self.current_num.startswith("."):
                    self.current_num = "0" + self.current_num

        self.display = self.current_num

    def _handle_plus_minus(self):
        if self.after_equals:
            return
        if self.current_num == "0":
            return
        if self.current_num.startswith("-"):
            self.current_num = self.current_num[1:]
        else:
            self.current_num = "-" + self.current_num
        self.display = self.current_num

    def _handle_percent(self):
        if self.after_equals:
            return
        try:
            val = float(self.current_num) / 100.0
            self.current_num = self._format_value(val)
            self.display = self.current_num
            self.has_decimal = "." in self.current_num
            self.is_typing = False
        except:
            pass

    def _handle_operator(self, key):
        if key == "=":
            if self.after_equals:
                return
            self._calculate()
            self.after_equals = True
        else:
            if self.last_operator is not None and self.is_typing:
                self._calculate()
            
            self.last_operator = key
            self.after_equals = False
            self.is_typing = False

    def _calculate(self):
        try:
            operand = float(self.current_num)

            if self.last_operator is None:
                self.running_total = operand
            else:
                if self.last_operator == "+":
                    self.running_total += operand
                elif self.last_operator == "-":
                    self.running_total -= operand
                elif self.last_operator == "*":
                    self.running_total *= operand
                elif self.last_operator == "/":
                    if operand == 0:
                        self.display = "0으로 나눌 수 없습니다"
                        self.is_error = True
                        return
                    self.running_total /= operand

            self.current_num = self._format_value(self.running_total)
            self.display = self.current_num
            self.is_typing = False
        except Exception:
            pass

class Calculator:
    def __init__(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _format_value(self, val):
        try:
            res = f"{round(val, 10):.10f}"
            if "." in res:
                res = res.rstrip('0').rstrip('.')
            if res == "-0":
                res = "0"
            return res if res != "" else "0"
        except Exception:
            return "0"

    def press(self, key: str) -> str:
        if self.is_error:
            if key == "C":
                self._reset()
                return self.display
            return self.display

        if key == "C":
            self._reset()
        elif key == "BS":
            self._handle_bs()
        elif key == "+/-":
            self._handle_plus_minus()
        elif key == "%":
            self._handle_percent()
        elif key in "0123456789.":
            self._handle_digit(key)
        elif key in "+-*/=":
            self._handle_operator(key)

        return self.display

    def _reset(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _handle_digit(self, key):
        if self.after_equals:
            self.current_num = ""
            self.running_total = 0.0
            self.last_operator = None
            self.after_equals = False
            self.is_typing = False
            self.has_decimal = False

        if key == ".":
            if not self.has_decimal:
                if self.current_num == "" or self.current_num == "0":
                    self.current_num = "0."
                else:
                    self.current_num += "."
                self.has_decimal = True
            return

        clean_num = self.current_num.replace(".", "").replace("-", "")
        if len(clean_num) < 12:
            if self.current_num == "0":
                self.current_num = key
            else:
                self.current_num += key
            self.is_typing = True

        if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
            self.current_num = self.current_num.lstrip("0")
            if self.current_num == "" or self.current_num.startswith("."):
                self.current_num = "0" + self.current_num

        self.display = self.current_num
        self.has_decimal = "." in self.current_num

    def _handle_bs(self):
        if self.after_equals:
            return

        if len(self.current_num) <= 1:
            self.current_num = "0"
            self.has_decimal = False
        else:
            self.current_num = self.current_num[:-1]
            if self.current_num == "" or self.current_num == "-":
                self.current_num = "0"
            if self.current_num.endswith("."):
                self.current_num = self.current_num[:-1]
                self.has_decimal = False
            
            if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
                self.current_num = self.current_num.lstrip("0")
                if self.current_num == "" or self.current_num.startswith("."):
                    self.current_num = "0" + self.current_num

        self.display = self.current_num

    def _handle_plus_minus(self):
        if self.after_equals:
            return
        if self.current_num == "0":
            return
        if self.current_num.startswith("-"):
            self.current_num = self.current_num[1:]
        else:
            self.current_num = "-" + self.current_num
        self.display = self.current_num

    def _handle_percent(self):
        if self.after_equals:
            return
        try:
            val = float(self.current_num) / 100.0
            self.current_num = self._format_value(val)
            self.display = self.current_num
            self.has_decimal = "." in self.current_num
            self.is_typing = False
        except:
            pass

    def _handle_operator(self, key):
        if key == "=":
            if self.after_equals:
                return
            self._calculate()
            self.after_equals = True
        else:
            if self.last_operator is not None and self.is_typing:
        else:
            if self.last_operator is not None and self.is_typing:
                self._calculate()
            
            self.last_operator = key
            self.after_equals = False
    def _calculate(self):
        try:
            operand = float(self.current_num)

            if self.last_operator is None:
                self.running_total = operand
            else:
                if self.last_operator == "+":
                    self.running_total += operand
                elif self.last_operator == "-":
                    self.running_total -= operand
                elif self.last_operator == "*":
                    self.running_total *= operand
                elif self.last_operator == "/":
                    if operand == 0:
                        self.display = "0으로 나눌 수 없습니다"
                        self.is_error = True
                        return
                    self.running_total /= operand

            self.current_num = self._format_value(self.running_total)
            self.display = self.current_num
            self.is_typing = False
        except Exception:
            pass

            self.is_typing = False

                self._calculate()
            
            self.last_operator = key
            self.after_equals = False
            self.is_typing = False

    def _calculate(self):
        try:
            operand = float(self.current_num)

            if self.last_operator is None:
                self.running_total = operand
            else:
                if self.last_operator == "+":
                    self.running_total += operand
                elif self.last_operator == "-":
                    self.running_total -= operand
                elif self.last_operator == "*":
                    self.running_total *= operand
                elif self.last_operator == "/":
                    if operand == 0:
                        self.display = "0으로 나눌 수 없습니다"
                        self.is_error = True
                        return
                    self.running_total /= operand

            self.current_num = self._format_value(self.running_total)
            self.display = self.current_num
            self.is_typing = False
        except Exception:
            pass

class Calculator:
    def __init__(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _format_value(self, val):
        try:
            res = f"{round(val, 10):.10f}"
            if "." in res:
                res = res.rstrip('0').rstrip('.')
            if res == "-0":
                res = "0"
            return res if res != "" else "0"
        except Exception:
            return "0"

    def press(self, key: str) -> str:
        if self.is_error:
            if key == "C":
                self._reset()
                return self.display
            return self.display

        if key == "C":
            self._reset()
        elif key == "BS":
            self._handle_bs()
        elif key == "+/-":
            self._handle_plus_minus()
        elif key == "%":
            self._handle_percent()
        elif key in "0123456789.":
            self._handle_digit(key)
        elif key in "+-*/=":
            self._handle_operator(key)

        return self.display

    def _reset(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _handle_digit(self, key):
        if self.after_equals:
            self.current_num = ""
            self.running_total = 0.0
            self.last_operator = None
            self.after_equals = False
            self.is_typing = False
            self.has_decimal = False

        if key == ".":
            if not self.has_decimal:
                if self.current_num == "" or self.current_num == "0":
                    self.current_num = "0."
                else:
                    self.current_num += "."
                self.has_decimal = True
            return

        clean_num = self.current_num.replace(".", "").replace("-", "")
        if len(clean_num) < 12:
            if self.current_num == "0":
                self.current_num = key
            else:
                self.current_num += key
            self.is_typing = True

        if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
            self.current_num = self.current_num.lstrip("0")
            if self.current_num == "" or self.current_num.startswith("."):
                self.current_num = "0" + self.current_num

        self.display = self.current_num
        self.has_decimal = "." in self.current_num

    def _handle_bs(self):
        if self.after_equals:
            return

        if len(self.current_num) <= 1:
            self.current_num = "0"
            self.has_decimal = False
        else:
            self.current_num = self.current_num[:-1]
            if self.current_num == "" or self.current_num == "-":
                self.current_num = "0"
            if self.current_num.endswith("."):
                self.current_num = self.current_num[:-1]
                self.has_decimal = False
            
            if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
                self.current_num = self.current_num.lstrip("0")
                if self.current_num == "" or self.current_num.startswith("."):
                    self.current_num = "0" + self.current_num

        self.display = self.current_num

    def _handle_plus_minus(self):
        if self.after_equals:
            return
        if self.current_num == "0":
            return
        if self.current_num.startswith("-"):
            self.current_num = self.current_num[1:]
        else:
            self.current_num = "-" + self.current_num
        self.display = self.current_num

    def _handle_percent(self):
        if self.after_equals:
            return
        try:
            val = float(self.current_num) / 100.0
            self.current_num = self._format_value(val)
            self.display = self.current_num
            self.has_decimal = "." in self.current_num
            self.is_typing = False
        except:
            pass

    def _handle_operator(self, key):
        if key == "=":
            if self.after_equals:
                return
            self._calculate()
            self.after_equals = True
        else:
            if self.last_operator is not None and self.is_typing:
                self._calculate()
            
            self.last_operator = key
            self.after_equals = False
            self.is_typing = False

    def _calculate(self):
        try:
            operand = float(self.current_num)

            if self.last_operator is None:
                self.running_total = operand
            else:
                if self.last_operator == "+":
                    self.running_total += operand
                elif self.last_operator == "-":
                    self.running_total -= operand
                elif self.last_operator == "*":
                    self.running_total *= operand
                elif self.last_operator == "/":
                    if operand == 0:
                        self.display = "0으로 나눌 수 없습니다"
                        self.is_error = True
                        return
                    self.running_total /= operand

            self.current_num = self._format_value(self.running_total)
            self.display = self.current_num
            self.is_typing = False
        except Exception:
            pass

class Calculator:
    def __init__(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _format_value(self, val):
        try:
            res = f"{round(val, 10):.10f}"
            if "." in res:
                res = res.rstrip('0').rstrip('.')
            if res == "-0":
                res = "0"
            return res if res != "" else "0"
        except Exception:
            return "0"

    def press(self, key: str) -> str:
        if self.is_error:
            if key == "C":
                self._reset()
                return self.display
            return self.display

        if key == "C":
            self._reset()
        elif key == "BS":
            self._handle_bs()
        elif key == "+/-":
            self._handle_plus_minus()
        elif key == "%":
            self._handle_percent()
        elif key in "0123456789.":
            self._handle_digit(key)
        elif key in "+-*/=":
            self._handle_operator(key)

        return self.display

    def _reset(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _handle_digit(self, key):
        if self.after_equals:
            self.current_num = ""
            self.running_total = 0.0
            self.last_operator = None
            self.after_equals = False
            self.is_typing = False
            self.has_decimal = False

        if key == ".":
            if not self.has_decimal:
                if self.current_num == "" or self.current_num == "0":
                    self.current_num = "0."
                else:
                    self.current_num += "."
                self.has_decimal = True
            return

        clean_num = self.current_num.replace(".", "").replace("-", "")
        if len(clean_num) < 12:
            if self.current_num == "0":
                self.current_num = key
            else:
                self.current_num += key
            self.is_typing = True

        if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
            self.current_num = self.current_num.lstrip("0")
            if self.current_num == "" or self.current_num.startswith("."):
                self.current_num = "0" + self.current_num

        self.display = self.current_num
        self.has_decimal = "." in self.current_num

    def _handle_bs(self):
        if self.after_equals:
            return

        if len(self.current_num) <= 1:
            self.current_num = "0"
            self.has_decimal = False
        else:
            self.current_num = self.current_num[:-1]
            if self.current_num == "" or self.current_num == "-":
                self.current_num = "0"
            if self.current_num.endswith("."):
                self.current_num = self.current_num[:-1]
                self.has_decimal = False
            
            if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
                self.current_num = self.current_num.lstrip("0")
                if self.current_num == "" or self.current_num.startswith("."):
                    self.current_num = "0" + self.current_num

        self.display = self.current_num

    def _handle_plus_minus(self):
        if self.after_equals:
            return
        if self.current_num == "0":
            return
        if self.current_num.startswith("-"):
            self.current_num = self.current_num[1:]
        else:
            self.current_num = "-" + self.current_num
        self.display = self.current_num

    def _handle_percent(self):
        if self.after_equals:
            return
        try:
            val = float(self.current_num) / 100.0
            self.current_num = self._format_value(val)
            self.display = self.current_num
            self.has_decimal = "." in self.current_num
            self.is_typing = False
        except:
            pass

    def _handle_operator(self, key):
        if key == "=":
            if self.after_equals:
                return
            self._calculate()
            self.after_equals = True
        else:
            if self.last_operator is not None and self.is_typing:
                self._calculate()
            
            self.last_operator = key
            self.after_equals = False
            self.is_typing = False

    def _calculate(self):
        try:
            operand = float(self.current_num)

            if self.last_operator is None:
                self.running_total = operand
            else:
                if self.last_operator == "+":
                    self.running_total += operand
                elif self.last_operator == "-":
                    self.running_total -= operand
                elif self.last_operator == "*":
                    self.running_total *= operand
                elif self.last_operator == "/":
                    if operand == 0:
                        self.display = "0으로 나눌 수 없습니다"
                        self.is_error = True
                        return
                    self.running_total /= operand

            self.current_num = self._format_value(self.running_total)
            self.display = self.current_num
            self.is_typing = False
        except Exception:
            pass

class Calculator:
    def __init__(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _format_value(self, val):
        """Rule 6: 소수 10자리에서 반올림하고, 끝의 0과 필요 없는 소수점은 떼어 낸다."""
        try:
            res = f"{round(val, 10):.10f}"
            if "." in res:
                res = res.rstrip('0').rstrip('.')
            if res == "-0":
                res = "0"
            return res if res != "" else "0"
        except Exception:
            return "0"

    def press(self, key: str) -> str:
        if self.is_error:
            if key == "C":
                self._reset()
                return self.display
            return self.display

        if key == "C":
            self._reset()
        elif key == "BS":
            self._handle_bs()
        elif key == "+/-":
            self._handle_plus_minus()
        elif key == "%":
            self._handle_percent()
        elif key in "0123456789.":
            self._handle_digit(key)
        elif key in "+-*/=":
            self._handle_operator(key)

        return self.display

    def _reset(self):
        self.display = "0"
        self.current_num = "0"
        self.running_total = 0.0
        self.last_operator = None
        self.is_error = False
        self.after_equals = False
        self.has_decimal = False
        self.is_typing = False

    def _handle_digit(self, key):
        if self.after_equals:
            self.current_num = ""
            self.running_total = 0.0
            self.last_operator = None
            self.after_equals = False
            self.is_typing = False
            self.has_decimal = False

        if key == ".":
            if not self.has_decimal:
                if self.current_num == "" or self.current_num == "0":
                    self.current_num = "0."
                else:
                    self.current_num += "."
                self.has_decimal = True
            return

        clean_num = self.current_num.replace(".", "").replace("-", "")
        if len(clean_num) < 12:
            if self.current_num == "0":
                self.current_num = key
            else:
                self.current_num += key
            self.is_typing = True

        if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
            self.current_num = self.current_num.lstrip("0")
            if self.current_num == "" or self.current_num.startswith("."):
                self.current_num = "0" + self.current_num

        self.display = self.current_num
        self.has_decimal = "." in self.current_num

    def _handle_bs(self):
        if self.after_equals:
            return

        if len(self.current_num) <= 1:
            self.current_num = "0"
            self.has_decimal = False
        else:
            self.current_num = self.current_num[:-1]
            if self.current_num == "" or self.current_num == "-":
                self.current_num = "0"
            if self.current_num.endswith("."):
                self.current_num = self.current_num[:-1]
                self.has_decimal = False
            
            if len(self.current_num) > 1 and self.current_num.startswith("0") and self.current_num[1] != ".":
                self.current_num = self.current_num.lstrip("0")
                if self.current_num == "" or self.current_num.startswith("."):
                    self.current_num = "0" + self.current_num

        self.display = self.current_num

    def _handle_plus_minus(self):
        if self.after_equals:
            return
        if self.current_num == "0":
            return
        if self.current_num.startswith("-"):
            self.current_num = self.current_num[1:]
        else:
            self.current_num = "-" + self.current_num
        self.display = self.current_num

    def _handle_percent(self):
        if self.after_equals:
            return
        try:
            val = float(self.current_num) / 100.0
            self.current_num = self._format_value(val)
            self.display = self.current_num
            self.has_decimal = "." in self.current_num
            self.is_typing = False
        except:
            pass

    def _handle_operator(self, key):
        if key == "=":
            if self.after_equals:
                return
            self._calculate()
            self.after_equals = True
        else:
            if self.last_operator is not None and self.is_typing:
                self._calculate()
            
            self.last_operator = key
            self.after_equals = False
            self.is_typing = False

    def _calculate(self):
        try:
            operand = float(self.current_num)

            if self.last_operator is None:
                self.running_total = operand
            else:
                if self.last_operator == "+":
                    self.running_total += operand
                elif self.last_operator == "-":
                    self.running_total -= operand
                elif self.last_operator == "*":
                    self.running_total *= operand
                elif self.last_operator == "/":
                    if operand == 0:
                        self.display = "0으로 나눌 수 없습니다"
                        self.is_error = True
                        return
                    self.running_total /= operand

            self.current_num = self._format_value(self.running_total)
            self.display = self.current_num
            self.is_typing = False
        except Exception:
            pass
