# def allcaps(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

# Example usage:
if __name__ == "__main__":
    @allcaps
    def greet():
        return "hello World!"

    def main():
        print(greet())

    main()
