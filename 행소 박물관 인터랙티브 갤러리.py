import tkinter as tk
from tkinter import messagebox

class FullInteractiveGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("🏛️ 계명대학교 행소박물관 인터랙티브 갤러리 (유물 10선)")
        self.root.geometry("650x760")  
        self.root.configure(bg="#f8f9fa")
        
        # 유물 설명과 더불어 '큐레이터 전용 심층 해설(detail_info)' 데이터를 완벽하게 추가 구축!
        self.artifacts = [
            {
                "title": "1. 청화 백자 봉황문 항아리 (조선 후기)",
                "description": "구름 속을 날고 있는 봉황을 대범하게 그려 넣은 항아리입니다. 왕실의 문양으로 사용되어 왕의 어진 정치와 나라의 평안함을 바라는 소망이 담겨 있습니다.",
                "color": "#e0f2f1", "type": "jar",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n이 항아리는 조선 후기 분원 관요에서 제작된 최고급 백자입니다. 닭의 머리, 뱀의 목, 원앙의 날개를 지닌 상상의 새 '봉황'이 푸른 청화 안료로 역동적으로 그려져 있습니다. 조선 시대에 봉황은 '태평성대'를 상징하며, 오직 왕실의 안녕과 국운 융성을 기원하는 의례용 기물에만 제한적으로 사용되던 문양입니다."
            },
            {
                "title": "2. 청자 상감 운봉문 대접 (고려시대)",
                "description": "안쪽 면에 구름 사이로 날고 있는 봉황을 새긴 후 백토로 채우고 유약을 입혀 구운 대접입니다. 고려 귀족 사회의 화려한 예술성을 보여줍니다.",
                "color": "#d0e1d4", "type": "bowl",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n고려 12-13세기 상감청자의 정수를 보여주는 작품입니다. 대접 안쪽에 구름과 봉황 문양을 정교하게 판 뒤, 백토를 채워 넣어 굽는 '상감 기법'이 정점인 시기에 만들어졌습니다. 푸른 비색 유약 아래로 은은하게 비치는 백색의 봉황은 당시 최고위 귀족층이나 왕실의 화려한 생활상을 그대로 대변합니다."
            },
            {
                "title": "3. 청화 백자 십장생문 병 (조선 후기)",
                "description": "몸통에 해, 구름, 사슴, 거북, 소나무 등 오래 사는 열 가지 상징물을 그려 넣은 병입니다. 옛사람들이 오래오래 건강하게 사는 삶을 소망했음을 알 수 있습니다.",
                "color": "#e3f2fd", "type": "bottle",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n조선 후기 민간과 왕실에서 크게 유행한 '장생 신앙'이 투영된 도자기입니다. 병의 둥근 몸통을 따라 해, 거북, 사슴, 불로초 등 불로장생을 뜻하는 십장생이 끊김 없이 연속적인 구도로 그려져 있습니다. 일상적인 병의 형태에 무병장수라는 인간의 가장 근원적인 염원을 예술적으로 담아낸 명작입니다."
            },
            {
                "title": "4. 봉황 자수 베갯모 (조선 후기)",
                "description": "붉은색 천 위에 암수 한 쌍의 봉황이 일곱 마리의 새끼를 거느린 모습을 수놓은 베갯모입니다. 자식을 많이 낳고 행복한 가정이 영원하길 바라는 마음이 담겨 신혼부부가 주로 사용했습니다.",
                "color": "#ffebee", "type": "embroidery",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n이 유물은 조선 시대 서민들의 삶과 염원이 담긴 자수 공예품입니다. 어미 봉황 한 쌍과 새끼 일곱 마리가 정교하게 수놓아져 있어 '구봉침'이라 불립니다. 전통 사회에서 다산(多産)과 가문의 번창, 그리고 신혼부부의 영원한 행복을 바라는 민간의 순수한 마취가 붉은 비단천 위 고운 오색 실 속에 그대로 녹아있습니다."
            },
            {
                "title": "5. 신석기 시대 빗살무늬 토기 (선사시대실)",
                "description": "대구/경북 지역에서 출토된 대표적인 선사시대 토기입니다. 표면에 기하학적인 빗살무늬가 새겨져 있으며 조상들의 정착 생활과 식생활 변화를 보여주는 중요한 유물입니다.",
                "color": "#efebe9", "type": "pottery",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n한반도 신석기 시대를 대표하는 유물로, 도구의 끝으로 토기 겉면에 기하학적인 도트와 사선을 새겼습니다. 밑바닥이 뾰족한 평저/첨저 형태는 강가나 해안가의 모래틀에 토기를 깊숙이 박아두고 음식을 저장하거나 조리하기 위한 최적의 생존 디자인이었습니다. 인류가 정착 생활을 시작했음을 알리는 위대한 첫걸음입니다."
            },
            {
                "title": "6. 가야 시대 오리모양 토기 (선사시대실)",
                "description": "오리의 모습을 본떠 만든 독특한 형태의 가야 토기입니다. 고대인들이 오리를 이승과 저승을 연결하는 신성한 새라고 믿어 죽은 이의 영혼을 위로하기 위해 무덤에 함께 묻었던 부장품입니다.",
                "color": "#f5f5f5", "type": "duck",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n가야 지역 무덤에서 주로 출토되는 '의례용 원삼국/가야 토기'입니다. 고대인들은 물 위를 날고 땅을 걸으며 물속을 헤엄치는 오리를 '이승과 저승, 인간과 하늘을 연결하는 영적인 매개체'로 보았습니다. 죽은 이의 영혼이 저승으로 무사히 날아가기를 바라는 고대인들의 내세관과 장례 문화를 엿볼 수 있는 귀중한 유물입니다."
            },
            {
                "title": "7. 청동기 시대 거친무늬 거울 (선사시대실)",
                "description": "청동기 시대의 권력자가 제사나 의례를 지낼 때 가슴에 매달았던 거울입니다. 뒷면에 정교한 기하학적 선 무늬가 새겨져 있어 고대 청동 주조 기술의 뛰어남을 보여줍니다.",
                "color": "#eceff1", "type": "mirror",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n이 유물은 얼굴을 비추는 거울이라기보다, 청동기 시대 최고 제사장(군장)이 의례를 행할 때 가슴에 걸치던 '신성한 권력의 상징물'입니다. 거울 앞면에 햇빛이 반사되어 번쩍이는 모습을 통해 제사장의 신성함을 군중에게 과시했습니다. 뒷면에 새겨진 거친 직선 문양들은 당시 고대 사회의 정교한 주조 합금 기술력을 입증합니다."
            },
            {
                "title": "8. 고려시대 청자 상감 모란문 매병 (고려/조선실)",
                "description": "S자 곡선의 아름다운 몸통 위에 부귀영화를 상징하는 모란꽃 무늬를 상감 기법으로 정교하게 장식한 고려시대의 대표적인 매병입니다.",
                "color": "#e0f2f1", "type": "maebyeong",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n좁은 목과 풍만한 어깨, 그리고 아래로 갈수록 매끈하게 좁아지는 S자 곡선미가 일품인 고려 매병입니다. 도자기 표면에 큼직하게 배치된 '모란' 문양은 동양 전통 예술에서 '부귀영화'와 '왕실의 번영'을 상징합니다. 흑백의 상감선이 청자의 비색과 강렬한 대비를 이루어 격조 높은 아름다움을 보여줍니다."
            },
            {
                "title": "9. 조선시대 분청사기 철화어문 항아리 (고려/조선실)",
                "description": "분장한 도자기 표면에 검은색 철안료를 사용하여 자유분방하고 해학적인 물고기 문양을 그려 넣은 조선 초기의 개성 넘치는 항아리입니다.",
                "color": "#f1f8e9", "type": "fish_jar",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n조선 15-16세기 계룡산 가마터 등지에서 주로 제작된 분청사기입니다. 백토를 바른 표면 위에 산화철 안료를 붓에 묻혀 물고기를 그렸는데, 정밀한 묘사보다는 대범하고 익살스럽게 표현된 점이 특징입니다. 양반가 도자기의 엄격함에서 벗어나 조선 초기 민중 예술의 자유분방함과 파격적인 현대적 미감을 느낄 수 있습니다."
            },
            {
                "title": "10. 조선시대 수묵 산수화 가리개 (고려/조선실)",
                "description": "먹의 짙고 옅은 농담만을 활용하여 대자연의 깊은 풍경과 선비의 기상을 표현한 회화 작품입니다. 자연과 동화되고자 했던 옛 선비들의 정신세계가 담겨 있습니다.",
                "color": "#fffde7", "type": "painting",
                "detail_info": "💡 [큐레이터 심층 해설]\n\n조선 시대 선비들의 방을 장식하던 문방 제구이자 예술품입니다. 화려한 채색을 배제하고 오직 먹 한 가지 색의 농담(진하고 옅음)과 붓의 필력만으로 첩첩산중과 흐르는 계곡을 그려냈습니다. 이는 세속의 권력에서 벗어나 대자연 속에 은거하며 학문에 정진하고 품격을 유지하고자 했던 조선 지식인들의 고고한 내면세계를 투영합니다."
            }
        ]
        
        self.current_index = 0
        self.create_widgets()
        self.update_gallery()

    def create_widgets(self):
        # 1. 상단 타이틀 바
        title_frame = tk.Frame(self.root, bg="#2c3e50", pady=15)
        title_frame.pack(fill="x")
        
        main_title = tk.Label(title_frame, text="행소박물관 인터랙티브 유물 갤러리 (10대 유물)", 
                              font=("Malgun Gothic", 16, "bold"), fg="white", bg="#2c3e50")
        main_title.pack()
        
        # 2. 그래픽스 캔버스 영역
        self.canvas_frame = tk.Frame(self.root, bg="#f8f9fa", pady=10)
        self.canvas_frame.pack()
        
        self.canvas = tk.Canvas(self.canvas_frame, width=350, height=330, bg="white", 
                                highlightthickness=2, highlightbackground="#cfd8dc")
        self.canvas.pack()
        
        # 3. 유물 이름 레이블
        self.title_label = tk.Label(self.root, text="", font=("Malgun Gothic", 15, "bold"), 
                                    fg="#16a085", bg="#f8f9fa")
        self.title_label.pack(pady=5)
        
        # 4. 유물 설명 레이블
        desc_frame = tk.Frame(self.root, bg="white", padx=15, pady=15, bd=1, relief="solid")
        desc_frame.pack(padx=30, pady=5, fill="x")
        
        self.desc_label = tk.Label(desc_frame, text="", font=("Malgun Gothic", 11), 
                                   fg="#34495e", bg="white", wraplength=520, justify="left")
        self.desc_label.pack()
        
        # 5. 제어 버튼 영역
        btn_frame = tk.Frame(self.root, bg="#f8f9fa", pady=15)
        btn_frame.pack(fill="x")
        
        self.info_btn = tk.Button(btn_frame, text="🏛️ 큐레이터 정밀 해설", font=("Malgun Gothic", 11, "bold"),
                                  bg="#3498db", fg="white", padx=10, pady=5, command=self.show_docent)
        self.info_btn.pack(side="left", padx=40)
        
        self.next_btn = tk.Button(btn_frame, text="▶ 다음 유물 이동", font=("Malgun Gothic", 11, "bold"),
                                  bg="#2ecc71", fg="white", padx=10, pady=5, command=self.next_artifact)
        self.next_btn.pack(side="right", padx=40)
        
        # 하단 진행도 표시 바
        self.page_label = tk.Label(self.root, text="", font=("Malgun Gothic", 9), fg="#7f8c8d", bg="#f8f9fa")
        self.page_label.pack(side="bottom", pady=5)

    def draw_artifact_geometry(self, data):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 350, 330, fill=data["color"], outline="")
        t = data["type"]
        
        if t == "jar": 
            self.canvas.create_oval(100, 80, 250, 280, fill="#ffffff", outline="#7f8c8d", width=3)
            self.canvas.create_rectangle(130, 40, 220, 80, fill="#ffffff", outline="#7f8c8d", width=3)
            self.canvas.create_text(175, 180, text="✨ [봉황문 항아리]", font=("Malgun Gothic", 11, "bold"), fill="#2c3e50")
        elif t == "bowl": 
            self.canvas.create_oval(60, 90, 290, 240, fill="#b2dfdb", outline="#004d40", width=3)
            self.canvas.create_text(175, 165, text="✨ [상감 운봉문 대접]", font=("Malgun Gothic", 11, "bold"), fill="#004d40")
        elif t == "bottle": 
            self.canvas.create_oval(110, 140, 240, 290, fill="#ffffff", outline="#1565c0", width=3)
            self.canvas.create_oval(145, 50, 205, 140, fill="#ffffff", outline="#1565c0", width=3)
            self.canvas.create_text(175, 210, text="✨ [십장생문 병]", font=("Malgun Gothic", 11, "bold"), fill="#1565c0")
        elif t == "embroidery": 
            self.canvas.create_oval(90, 80, 260, 250, fill="#ff8a80", outline="#b71c1c", width=5)
            self.canvas.create_text(175, 165, text="✨ [봉황 자수 베갯모]", font=("Malgun Gothic", 11, "bold"), fill="#b71c1c")
        elif t == "pottery": 
            self.canvas.create_polygon([175, 280, 90, 70, 260, 70], fill="#bcaaa4", outline="#5d4037", width=3)
            for y in range(90, 250, 25):
                self.canvas.create_line(130, y, 220, y+10, fill="#5d4037", width=1)
            self.canvas.create_text(175, 140, text="✨ [빗살무늬 토기]", font=("Malgun Gothic", 11, "bold"), fill="#5d4037")
        elif t == "duck": 
            self.canvas.create_oval(110, 120, 240, 240, fill="#b0bec5", outline="#37474f", width=3)
            self.canvas.create_oval(210, 80, 260, 140, fill="#b0bec5", outline="#37474f", width=3) 
            self.canvas.create_rectangle(150, 240, 170, 280, fill="#37474f") 
            self.canvas.create_rectangle(180, 240, 200, 280, fill="#37474f")
            self.canvas.create_text(175, 180, text="✨ [오리모양 토기]", font=("Malgun Gothic", 11, "bold"), fill="#37474f")
        elif t == "mirror": 
            self.canvas.create_oval(90, 70, 260, 240, fill="#cfd8dc", outline="#455a64", width=5)
            self.canvas.create_oval(160, 140, 190, 170, fill="#455a64", outline="") 
            self.canvas.create_text(175, 270, text="✨ [거친무늬 청동거울]", font=("Malgun Gothic", 11, "bold"), fill="#455a64")
        elif t == "maebyeong": 
            self.canvas.create_oval(110, 70, 240, 190, fill="#80cbc4", outline="#004d40", width=3)
            self.canvas.create_oval(125, 150, 225, 280, fill="#80cbc4", outline="#004d40", width=3)
            self.canvas.create_text(175, 160, text="✨ [청자 상감 매병]", font=("Malgun Gothic", 11, "bold"), fill="#004d40")
        elif t == "fish_jar": 
            self.canvas.create_oval(100, 90, 250, 270, fill="#eeeeee", outline="#5d4037", width=3)
            self.canvas.create_line(120, 170, 230, 170, fill="#5d4037", width=3) 
            self.canvas.create_text(175, 140, text="✨ [분청사기 철화어문]", font=("Malgun Gothic", 11, "bold"), fill="#5d4037")
        elif t == "painting": 
            self.canvas.create_rectangle(60, 50, 290, 250, fill="#fff9c4", outline="#5d4037", width=6)
            self.canvas.create_line(90, 200, 160, 100, fill="#212121", width=3)
            self.canvas.create_line(150, 220, 240, 130, fill="#616161", width=4)
            self.canvas.create_text(175, 275, text="✨ [수묵 산수화 가리개]", font=("Malgun Gothic", 11, "bold"), fill="#212121")

    def update_gallery(self):
        data = self.artifacts[self.current_index]
        self.title_label.config(text=data["title"])
        self.desc_label.config(text=data["description"])
        
        self.draw_artifact_geometry(data)
        self.page_label.config(text=f"전체 10대 유물 관람 진행도: {self.current_index + 1} / {len(self.artifacts)}")

    def next_artifact(self):
        self.current_index = (self.current_index + 1) % len(self.artifacts)
        self.update_gallery()
        
    def show_docent(self):
        # [★정밀 해설 업그레이드] 현재 유물의 고유한 detail_info를 팝업창에 띄움!
        data = self.artifacts[self.current_index]
        messagebox.showinfo("🎓 큐레이터 전문 독점 해설", data["detail_info"])

if __name__ == "__main__":
    root = tk.Tk()
    app = FullInteractiveGallery(root)
    root.mainloop()
