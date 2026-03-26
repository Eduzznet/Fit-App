# treinos.py

workouts = {
    "Treino A": [
        {
            "tipo": "conjugado",
            "series": 1,
            "feitas": 0,
            "exercicios": [
                {"nome": "Rotação Interna de Ombro no Cross", "reps": "10/10", "video": "https://www.youtube.com/watch?v=9jS0CyZ4bL4"},
                {"nome": "Rotação Externa de Ombro no Cross", "reps": "10/10", "video": "https://www.youtube.com/watch?v=qczjEeYrono"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 3,
            "feitas": 0,
            "exercicios": [
                {"nome": "Supino Reto com Barra", "reps": "8/6/6/4", "video": "https://www.youtube.com/shorts/ZTZ-V5dEI24"},
                {"nome": "Abdominal Remador com Carga", "reps": 10, "video": "https://www.youtube.com/shorts/xMiylmYfU4A"},
                {"nome": "Flexão de Ombro com Halter", "reps": 10, "video": "https://www.youtube.com/shorts/zQstZDDVU4k"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 3,
            "feitas": 0,
            "exercicios": [
                {"nome": "Agachamento com Barra", "reps": "8/6/6/4", "video": "https://www.youtube.com/watch?v=WLw3eRGkM5U"},
                {"nome": "Wall Sit Witch Calf Raises", "reps": 20, "video": "https://www.youtube.com/shorts/gUTBnFKpkAQ"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 3,
            "feitas": 0,
            "exercicios": [
                {"nome": "Desenvolvimento Arnold", "reps": "8/8/6/6", "video": "https://www.youtube.com/watch?v=YghvTx_GI2c"},
                {"nome": "Abdominal Russo com Anilha", "reps": 20, "video": "https://www.youtube.com/shorts/olm_ljiNies"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 2,
            "feitas": 0,
            "exercicios": [
                {"nome": "Cadeira Extensora (Drop Set)", "reps": "10/8", "video": "https://www.youtube.com/shorts/q0q66CACEuM"},
                {"nome": "Abdução de Ombro", "reps": "10-8", "video": "https://www.youtube.com/shorts/_DuYa_M7U2I"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 2,
            "feitas": 0,
            "exercicios": [
                {"nome": "Afundo com Halter", "reps": "8/8", "video": "https://www.youtube.com/watch?v=6SHmjfEAwe0"},
                {"nome": "Triceps no Cross com Barra Reta", "reps": "10-8", "video": "https://www.youtube.com/shorts/ronI569Q9A4"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 2,
            "feitas": 0,
            "exercicios": [
                {"nome": "Cadeira Adutora", "reps": "12-10", "video": "https://www.youtube.com/shorts/lsb18p3cOAk"},
                {"nome": "Prancha Dinamica", "reps": 12, "video": "https://www.youtube.com/shorts/aXeVdfAaVRE?si=s5TtgwulBm_63aWs"}
            ]
        },
        {
            "tipo": "simples",
            "exercicios": [
                {"nome": "Circuito(Deslocamento Frente e Trás / Deslocamento Lateral / Deslocamento Triângulo / Agachamento com Salto)", "series": 2, "reps": "Tabata", "feitas": 0, "usa_carga": False}
            ]
        }
    ],
    "Treino B": [
        {
            "tipo": "conjugado",
            "series": 3,
            "feitas": 0,
            "exercicios": [
                {
                    "is_alternativo": True, 
                    "opcoes": [
                        {"nome": "Puxada Aberta no Pulley", "reps": "[6/6/4/4]","video": "https://www.youtube.com/shorts/MG3EbR-FOm4"},
                        {"nome": "Barra Fixa", "reps": "6-4", "video": "https://www.youtube.com/watch?v=HRV5YKKaeVw"}
                    ],
                },
                {
                    "nome": "Superman Alternado", 
                    "reps": "20", 
                    "video": "https://www.youtube.com/shorts/I-xM6bGr1y8"
                }
            ]
        },
        {
            "tipo": "conjugado",
            "series": 3,
            "feitas": 0,
            "exercicios": [
                {"nome": "Stiff com Barra ou Halter", "reps": "[8/8/6/6]", "video": "https://www.youtube.com/shorts/N55yUjeWp4A"},
                {"nome": "Flexão de Punho com Halter", "reps": 10, "video": "https://www.youtube.com/shorts/OWlt6mXm_Yc"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 3,
            "feitas": 0,
            "exercicios": [
                {"nome": "Remada Curvada com Halter", "reps": "[10/8/8/6]", "video": "https://www.youtube.com/shorts/j-OssGQT9kg"},
                {"nome": "Bíceps com Rotação", "reps": "10 -8 -8", "video": "https://www.youtube.com/shorts/KTkIE0HH-j8"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 2,
            "feitas": 0,
            "exercicios": [
                {"nome": "Cadeira Flexora", "reps": "[10/8]", "video": "https://www.youtube.com/shorts/RNxjVs8l55k"},
                {"nome": "Crucifixo Invertido Com Halter", "reps": "12 -10", "video": "https://www.youtube.com/watch?v=qGrI_BqZB0U"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 2,
            "feitas": 0,
            "exercicios": [
                {"nome": "Remada Alta com Halter", "reps": "10 -8", "video": "https://www.youtube.com/watch?v=vW--lca6Knw"},
                {"nome": "Extensão de Ombro no Cross com Barra", "reps": "10 -8", "video": "https://www.youtube.com/watch?v=p0gLwFQ8liA"}
            ]
        },
        {
            "tipo": "conjugado",
            "series": 2,
            "feitas": 0,
            "exercicios": [
                {"nome": "Cadeira Abdutora", "reps": "12 -10", "video": "https://www.youtube.com/shorts/445U95few3w"},
                {"nome": "Glute Bridge Walkout", "reps": 10, "video": "https://www.youtube.com/watch?v=NaisR71dDxI"}
            ]
        },
        {
            "tipo": "simples",
            "exercicios": [
                {"nome": "Bike Spinning", "series": 1, "reps": "Tabata", "feitas": 0, "usa_carga": False}
            ]
        }
    ],
    "Mobilidade": {
        "Treino 1": [
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Ombro com Elástico", "series": 1, "reps": 15, "feitas": 0, "video": "https://www.youtube.com/watch?v=dLWh8g3v5QE", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Russian Babymakers", "series": 1, "reps": "45''", "feitas": 0, "video": "https://www.youtube.com/watch?v=GiKENv5Rgqg", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Down Dog to Up Dog", "series": 1, "reps": 10, "feitas": 0, "video": "https://www.youtube.com/watch?v=zbG9LQst6EA", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Cat and Cow", "series": 1, "reps": 15, "feitas": 0, "video": "https://www.youtube.com/watch?v=ESJ6Ghvgr6k", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Mobilidade Quadril", "series": 1, "reps": "40'' cada", "feitas": 0, "video": "https://www.youtube.com/shorts/NcC0EttCXKw", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Butterfly Strech", "series": 1, "reps": "45''", "feitas": 0, "video": "https://www.youtube.com/watch?v=cfJcO7gi3zw", "usa_carga": False}
                ]
            }
        ],
        "Treino 2": [
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Thoracic Rotation", "series": 1, "reps": "8/8", "feitas": 0, "video": "https://www.youtube.com/watch?v=EHZJns1bXPM", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Wristles", "series": 1, "reps": "30''", "feitas": 0, "video": "https://www.youtube.com/watch?v=QiMiia4F7Xg", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Puppy Stretch", "series": 1, "reps": "40''", "feitas": 0, "video": "https://www.youtube.com/watch?v=VM87l97X7gY", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "90/90", "series": 1, "reps": "40''", "feitas": 0, "video": "https://www.youtube.com/watch?v=m51AZSXMvEA", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Knuckle Drags", "series": 1, "reps": 20, "feitas": 0, "video": "https://www.youtube.com/watch?v=yWXQ_vRVXZw", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Scorpion", "series": 1, "reps": "40''", "feitas": 0, "video": "https://www.youtube.com/watch?v=q9Sllm2jEss", "usa_carga": False}
                ]
            }
        ]
    },
    
    "Preventivo": {
        "Prevenção de Joelho": [
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Passagem de Halter", "series": 1, "reps": "12/12", "feitas": 0, "video": "https://www.instagram.com/p/DKSBof2tAI_/?img_index=5"}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Desaceleração sem carga", "series": 1, "reps": "6/6", "feitas": 0, "video": "https://www.instagram.com/p/DNUWSWqTyt7/?img_index=4", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Reverse Lunge Knee Dive", "series": 1, "reps": "6/6", "feitas": 0, "video": "https://www.youtube.com/shorts/cUJc9ZaSqbU", "usa_carga": False}
                ]
            },
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Salto + Aterrisagem", "series": 1, "reps": "6/6", "feitas": 0, "video": "https://www.instagram.com/p/DN6bqryDTqi/", "usa_carga": False}
                ]
            }
        ],
        "Fortalecimentos": [
            # --- SEÇÃO JOELHO ---
            {"tipo": "titulo", "texto": "🦵 JOELHO"},
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Standing Knee Extension", "series": 1, "reps": "8/8", "video": "https://www.instagram.com/p/C9-AgKzIi0l/?img_index=3", "usa_carga": False},
                    {"nome": "Flexão de Quadril com Caneleira", "series": 1, "reps": "8/8", "video": "https://www.instagram.com/p/C9-AgKzIi0l/?img_index=3"},
                    {"nome": "Abdução Lateral com Caneleira]", "series": 1, "reps": "8/8", "video": "https://www.instagram.com/p/C-QHEkTTfDp/?img_index=5"}
                ]
            },
            
            # --- SEÇÃO TORNOZELO ---
            {"tipo": "titulo", "texto": "🦶 TORNOZELO"},
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "SL Soleus Eccentrics", "series": 2, "reps": "8/8", "video": "https://www.instagram.com/p/DEFxmYtxSdQ/?img_index=2", "usa_carga": False},
                    {"nome": "Eversão / Inversão / Dorsiflexão Resistida", "series": 2, "reps": "8/8/8", "video": "https://www.instagram.com/p/C4Dh1u7xeaP/", "usa_carga": False},
                    {"nome": "Single Leg Weighted Passs", "series": 2, "reps": "20/20", "video": "https://www.instagram.com/p/DAySRJgTJsn/?img_index=10"}
                ]
            },
            
            # --- SEÇÃO OMBRO ---
            {"tipo": "titulo", "texto": "💪 OMBRO"},
            {
                "tipo": "simples",
                "exercicios": [
                    {"nome": "Banded External Rotation", "series": 2, "reps": "10", "video": "https://www.instagram.com/p/DAvf66yTpDI/?img_index=2", "usa_carga": False},
                    {"nome": "Banded Diagonals", "series": 2, "reps": "8/8", "video": "https://www.instagram.com/p/DAvf66yTpDI/?img_index=4", "usa_carga": False},
                    {"nome": "Banded Y", "series": 2, "reps": "8/8", "video": "https://www.instagram.com/p/DAvf66yTpDI/?img_index=5",  "usa_carga": False},
                    {"nome": "Rotação controlada com Halter [Qualquer carga]", "series": 2, "reps": "6/6", "video": "https://www.instagram.com/p/DLFV-BUNZHs/"}
                ]
            }
        ]
    },
    
    "Alongamento": [
        {
            "tipo": "simples",
            "exercicios": [
                {"nome": "Superiores", "series": 1, "reps": "N/A", "feitas": 0, "video": "https://www.youtube.com/watch?v=QCAev2GSz2c", "usa_carga": False}
            ]
        },
        {
            "tipo": "simples",
            "exercicios": [
                {"nome": "Inferiores", "series": 1, "reps": "N/A", "feitas": 0, "video": "https://www.youtube.com/watch?v=dwJKxbZM46Y", "usa_carga": False}
            ]
        },
        {
            "tipo": "simples",
            "exercicios": [
                {"nome": "Lombar", "series": 1, "reps": "N/A", "feitas": 0, "video": "https://www.youtube.com/watch?v=xuE_srFfKvU&t=95s", "usa_carga": False}
            ]
        }
    ]
}