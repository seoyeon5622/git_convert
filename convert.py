def p6_to_p3(input_path, output_path):
    with open(input_path, "rb") as f:
        # 헤더 읽기
        header = []
        while len(header) < 4:
            line = f.readline()
            if line.startswith(b'#'):  # 주석 건너뛰기
                continue
            header.extend(line.strip().split())
        width, height, maxval = map(int, header[1:4])

        # 픽셀 데이터 읽기
        pixels = f.read()

    # P3 포맷으로 저장
    with open(output_path, "w") as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n{maxval}\n")
        for i in range(0, len(pixels), 3):
            r, g, b = pixels[i], pixels[i+1], pixels[i+2]
            f.write(f"{r} {g} {b}\n")

# 실행
p6_to_p3("/home/data/colorP6File.ppm", "colorP3File.ppm")


