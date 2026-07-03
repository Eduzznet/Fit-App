"""
Módulo de Dados (treinos.py)
Atua como um banco de dados estático em memória para o aplicativo.
A estrutura é dividida em dados atemporais (treinos_fixos) e dados sazonais (meses).
"""

# ==========================================
# TREINOS FIXOS
# Rotinas de base que raramente sofrem alterações entre os ciclos.
# Mantidos isolados para evitar redundância de dados nas planilhas mensais.
# ==========================================

treinos_fixos = {
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

# ==========================================
# PLANILHAS MENSAIS (SAZONAIS)
# Rotinas ativas que mudam a cada novo ciclo de preparação física.
# ==========================================
meses = {
    "Março 2026": {
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
        ]
    },

    "Abril 2026": {
        "Academia": {
            "Treino A": [
                {
                    "tipo": "conjugado",
                    "series": 1,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Rotação Interna no Cross", "reps": "8/8", "video": "https://www.youtube.com/shorts/n-VPL7NrxNQ"},
                        {"nome": "Rotação Externa no Cross", "reps": "8/8", "video": "https://www.youtube.com/shorts/0IOuexFOqBg"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Shoulder Care", "reps": "8/8", "video": "https://www.instagram.com/p/DU8Z4pajLDR/"},
                        {"nome": "Abdução Excêntrica", "reps": "8/8", "video": "https://www.instagram.com/p/DU8Z4pajLDR/"},
                        {"nome": "Plyo Single Leg Calf Raises", "reps": "10/10"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Db Plyo Press", "reps": "8", "video": "https://www.youtube.com/shorts/yLt97SKo-9I"},
                        {"nome": "Bench Plyo Push Ups", "reps": "8", "video": "https://www.youtube.com/shorts/zHqxyD9_364"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Barbell Box Squat", "reps": "6", "video": "https://www.instagram.com/p/DSsRoK4jKK4/"},
                        {"nome": "Drop To Broad Jump", "reps": "8", "video": "https://www.instagram.com/p/DPzpvfPkne6/"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Single Arm Hang Db Power Snatch", "reps": "6/6", "video": "https://www.youtube.com/watch?v=O3E77RfurAM"},
                        {"nome": "1/2 Kneeling Plate Chop Up", "reps": "8/8", "video": "https://www.youtube.com/shorts/OKIIPHiew24"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Db Lunge To Knee Drive [Fazer com velocidade]", "reps": "6/6", "video": "https://www.youtube.com/shorts/6vcsnby-RKg"},
                        {"nome": "Tríceps Extension", "reps": "12", "video": "https://www.youtube.com/shorts/RGtxl2g4ZoU"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Lateral Lunge Drop from Box", "reps": "8/8", "video": "https://www.youtube.com/shorts/A-01aEKyDb8"},
                        {"nome": "Alt. Db Front Raises", "reps": "16", "video": "https://www.youtube.com/shorts/dQp_WsdDMQI"}
                    ]
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Bike Spinning", "series": 1, "reps": "Tabata [8 x 20\"/10\"]", "feitas": 0, "usa_carga": False}
                    ]
                }
            ],
            "Treino B": [
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Jump Pull Up", "reps": "6", "video": "https://www.youtube.com/shorts/BLX0O9t51oQ"},
                        {"nome": "Superman Alternado", "reps": "20", "video": "https://www.youtube.com/shorts/EflwiA9kxm4"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Db Sumo Deadlift High Pull", "reps": "8", "video": "https://www.youtube.com/shorts/tdQULPBRAZU"},
                        {"nome": "V Up Alternado", "reps": "20", "video": "https://www.youtube.com/shorts/KbE-9_ticlo"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Pendlay Row", "reps": "6", "video": "https://www.youtube.com/shorts/tYxEGi7ir4I"},
                        {"nome": "Db Hang Power Clean", "reps": "8", "video": "https://www.youtube.com/shorts/7JtIMXUmgmc"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Plate Pullover", "reps": "6", "video": "https://www.youtube.com/watch?v=FK4rHfWKEac"},
                        {"nome": "Db T Raise", "reps": "8", "video": "https://www.youtube.com/watch?v=YsbzKsqfxYQ"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Db/Kb Split Stance [Pode Usar Kb ou Halter]", "reps": "6/6", "video": "https://www.youtube.com/shorts/LHR4UFuHHcc"},
                        {"nome": "Cadeira Abdutora 2 Tempos", "reps": "10", "video": "https://www.youtube.com/shorts/vv25W3Gj6aQ"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Single Leg Plyo Hip Thrust", "reps": "8/8", "video": "https://www.youtube.com/shorts/y2gq68ycDKc"},
                        {"nome": "Bíceps \"Plio\" Bilateral", "reps": "10", "video": "https://www.instagram.com/p/DH6goq3NlCv/"}
                    ]
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Corrida/Transport", "series": 1, "reps": "Tabata [8 x 20\"/10\"]", "feitas": 0, "usa_carga": False}
                    ]
                }
            ]
        },
        "Elástico e Peso Corporal": {
            "Treino A": [
                {
                    "tipo": "conjugado",
                    "series": 1,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Rotação Interna com Elástico", "reps": "10/10", "video": "https://www.youtube.com/shorts/8EyB6C54BPc", "usa_carga": False},
                        {"nome": "Rotação Externa com Elástico", "reps": "10/10", "video": "https://www.youtube.com/shorts/axDgHPuurjQ", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Bench Plyo Push Ups", "reps": "8", "video": "https://www.youtube.com/shorts/zHqxyD9_364", "usa_carga": False},
                        {"nome": "Plyo Single Leg Calf Raises", "reps": "12", "video": "https://www.youtube.com/shorts/ooGfKQ8lAhM", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Jump Squat", "reps": "8", "video": "https://www.youtube.com/watch?v=RLlFlaP4JFs", "usa_carga": False},
                        {"nome": "Drop To Broad Jump", "reps": "10", "video": "https://www.instagram.com/p/DPzpvfPkne6/", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Single Arm Snatch", "reps": "8/8", "video": "https://www.youtube.com/watch?v=NmxMriSlZBQ", "usa_carga": False},
                        {"nome": "Half Kneeling Band Chop", "reps": "10/10", "video": "https://www.youtube.com/shorts/ftQ4xaQoVKY", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Reverse Lunge With High Knee Drive", "reps": "8/8", "video": "https://www.youtube.com/shorts/mtTuOe23XdI", "usa_carga": False},
                        {"nome": "Band Tríceps [Fazer Veloz]", "reps": "10", "video": "https://www.youtube.com/shorts/vV1ukiLSZZc", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Lateral Lunge Drop from Box", "reps": "8/8", "video": "https://www.youtube.com/shorts/A-01aEKyDb8", "usa_carga": False},
                        {"nome": "Alt. Band Front Raises [Alternado]", "reps": "16", "video": "https://www.youtube.com/shorts/pYVlZiu2Mps", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "titulo",
                    "texto": "💦 Cardio 1: 2 Tabatas (8 x 30\"on / 10\"off)"
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Passada Handebol", "series": 2, "reps": "Tabata", "usa_carga": False},
                        {"nome": "Deslocamento Triângulo", "series": 2, "reps": "Tabata", "video": "https://www.youtube.com/shorts/mkNBqb51hPM", "usa_carga": False},
                        {"nome": "Deslocamento Frente e Trás", "series": 2, "reps": "Tabata", "video": "https://www.youtube.com/shorts/tGpiicrGP60", "usa_carga": False},
                        {"nome": "Mountain Climbers", "series": 2, "reps": "Tabata", "video": "https://www.youtube.com/watch?v=ruQ4ZwncXBg", "usa_carga": False}
                    ]
                }
            ],
            "Treino B": [
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Explosive Band Rows", "reps": "10", "video": "https://www.youtube.com/shorts/lZogIrhTazQ", "usa_carga": False},
                        {"nome": "Superman Alternado", "reps": "20", "video": "https://www.youtube.com/shorts/EflwiA9kxm4", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Banded Sumo Deadlift High Pull", "reps": "8", "video": "https://www.youtube.com/watch?v=G_YGop6nCn8", "usa_carga": False},
                        {"nome": "V Up Alternado", "reps": "20", "video": "https://www.youtube.com/shorts/KbE-9_ticlo", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Pull Down [Fazer Veloz]", "reps": "10", "video": "https://www.youtube.com/shorts/ymWqQboF2UE", "usa_carga": False},
                        {"nome": "Band Pull Apparts", "reps": "10", "video": "https://www.youtube.com/shorts/SuvO4TBwSu4", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Banded Single Leg RDL [Fazer Veloz]", "reps": "8/8", "video": "https://www.youtube.com/shorts/p7EQ4YaRv7c", "usa_carga": False},
                        {"nome": "Plank", "reps": "30\"", "video": "https://www.youtube.com/shorts/O83fmDwTYpg", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Banded Hip Abduction", "reps": "8/8", "video": "https://www.youtube.com/shorts/UCVP0qaHzN8", "usa_carga": False},
                        {"nome": "Superman Hold", "reps": "20\"", "video": "https://www.youtube.com/watch?v=tYMHYWVvFjs", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Single Leg Plyo Hip Thrust", "reps": "8/8", "video": "https://www.youtube.com/shorts/y2gq68ycDKc", "usa_carga": False},
                        {"nome": "Banded Band Curls [Fazer Veloz]", "reps": "10", "video": "https://www.youtube.com/watch?v=0hZboUNuogA", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "titulo",
                    "texto": "💦 Cardio 2"
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Aquecer 3' [Trote] + 12 Tiros 40m [Descanso 1']", "series": 1, "reps": "12 Tiros", "usa_carga": False}
                    ]
                }
            ]
        }
    },

    "Maio 2026": {
        "Academia": {
            "Treino A": [
                {
                    "tipo": "conjugado",
                    "series": 1,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Rotação Interna no Cross", "reps": "8/8", "video": "https://www.youtube.com/shorts/n-VPL7NrxNQ"},
                        {"nome": "Rotação Externa no Cross", "reps": "8/8", "video": "https://www.youtube.com/shorts/0IOuexFOqBg"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Landmine Single Arm Press [Se não tiver suporte, usar um canto]", "reps": "6/6", "video": "https://www.instagram.com/p/DWeDLP_jMAY/?img_index=4"},
                        {"nome": "Landmine Rotation", "reps": "12 [Alternado]", "video": "https://www.instagram.com/p/DWeDLP_jMAY/?img_index=5"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Explosive Pistol", "reps": "6/6", "video": "https://www.instagram.com/p/DVgcueYFqB5/"},
                        {"nome": "Step Jump", "reps": "6/6", "video": "https://www.instagram.com/p/DVgcueYFqB5/"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Explosive Bench Press", "reps": "8", "video": "https://www.instagram.com/p/DVgcueYFqB5"},
                        {"nome": "Plate Drop Push Up", "reps": "6", "video": "https://www.instagram.com/p/DK1_In9pGjN/"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Bound Lateral", "reps": "4/4", "video": "https://www.instagram.com/p/DWuf7Eajj81/"},
                        {"nome": "Exercício 13", "reps": "4/4", "video": "https://www.instagram.com/p/DUVxvgMCF9A/"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Tríceps OH Extensions Plyo", "reps": "10", "video": "https://www.instagram.com/p/DU8cyNliNpr/?img_index=7"},
                        {"nome": "Db T Raise [Veloz]", "reps": "10", "video": "https://www.youtube.com/watch?v=YsbzKsqfxYQ"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Db Jumps", "reps": "10", "video": "https://www.instagram.com/p/DUlJ1xYiKTd/?img_index=10"},
                        {"nome": "Plyo Calfs on Plate", "reps": "12", "video": "https://www.instagram.com/p/DVgcueYFqB5/"}
                    ]
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Bike Spinning", "series": 2, "reps": "Tabata [8 x 20\"/10\"]", "feitas": 0, "usa_carga": False}
                    ]
                }
            ],
            "Treino B": [
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Prone Db Drops", "reps": "10", "video": "https://www.instagram.com/p/C8PJClxtgYC/"},
                        {"nome": "Plate Plyo Pullover", "reps": "8", "video": "https://www.youtube.com/watch?v=FK4rHfWKEac"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Dual Db Swing [Pode usar halter]", "reps": "8", "video": "https://www.instagram.com/p/DV1Hd0EDHMo/"},
                        {"nome": "Kettlebell Pull Throughs [Pode usar halter]", "reps": "6/6", "video": "https://www.instagram.com/p/DQ9tTjLD0o1/"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Single Arm Explosive Row", "reps": "6/6", "video": "https://www.youtube.com/watch?v=XN0zhsSvhAU"},
                        {"nome": "Sumo Deadlift High Pull [Veloz]", "reps": "8", "video": "https://www.youtube.com/watch?v=gh55vVlwlQg"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Landmine Rotation", "reps": "6/6", "video": "https://www.instagram.com/p/COP5Z2bFlIC/"},
                        {"nome": "Swisse Ball Glute Bridge Walkout", "reps": "10", "video": "https://www.youtube.com/watch?v=xkYLi4f_NwQ"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Bíceps Excêntrico Unilateral", "reps": "4 à 6/lado", "video": "https://www.instagram.com/p/DH6goq3NlCv/"},
                        {"nome": "Bíceps \"Plio\" Bilateral", "reps": "10", "video": "https://www.instagram.com/p/DH6goq3NlCv/"}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 2,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Plate Russian Twist", "reps": "20", "video": "https://www.youtube.com/watch?v=4p5jWyz-YRQ"},
                        {"nome": "Db Split Stance Deadlift [Veloz]", "reps": "8/8", "video": "https://www.youtube.com/watch?v=LBzxZCUZrNA"}
                    ]
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Corrida/Transport", "series": 2, "reps": "Tabata [8 x 20\"/10\"]", "feitas": 0, "usa_carga": False}
                    ]
                }
            ]
        },
        "Elástico e Peso Corporal": {
            "Treino A": [
                {
                    "tipo": "conjugado",
                    "series": 1,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Rotação Interna com Elástico", "reps": "10/10", "video": "https://www.youtube.com/shorts/8EyB6C54BPc", "usa_carga": False},
                        {"nome": "Rotação Externa com Elástico", "reps": "10/10", "video": "https://www.youtube.com/shorts/axDgHPuurjQ", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Desenvolvimento Unilateral com Elástico", "reps": "6/6", "video": "https://www.youtube.com/shorts/hU1TpgGpISU", "usa_carga": False},
                        {"nome": "Pallof Press Rotation", "reps": "8/8", "video": "https://www.youtube.com/shorts/iAWKyMczcrs", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Explosive Pistol", "reps": "6/6", "video": "https://www.instagram.com/p/DVgcueYFqB5/", "usa_carga": False},
                        {"nome": "Step Jump", "reps": "6/6", "video": "https://www.instagram.com/p/DVgcueYFqB5/", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Explosive Band Bench Press", "reps": "8", "video": "https://www.youtube.com/shorts/dLzT_klXhro", "usa_carga": False},
                        {"nome": "Drop Push Up", "reps": "8", "video": "https://www.youtube.com/shorts/ftTjW4Fc3Xc", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Jump Squat", "reps": "8", "video": "https://www.youtube.com/watch?v=dF3B0ZviUfw", "usa_carga": False},
                        {"nome": "Calf Jump", "reps": "12", "video": "https://www.youtube.com/watch?v=JFQaPQk819k", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Plyo Tríceps Extensions [Veloz]", "reps": "10", "video": "https://www.youtube.com/watch?v=8-q04odgg4M", "usa_carga": False},
                        {"nome": "Band T Raise", "reps": "8", "video": "https://www.youtube.com/shorts/fF9rFT1dwi0", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "titulo",
                    "texto": "💦 Cardio 1: 2 Tabatas (8 x 30\"on / 10\"off)"
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Passada Handebol", "series": 2, "reps": "Tabata", "usa_carga": False},
                        {"nome": "Deslocamento Triângulo", "series": 2, "reps": "Tabata", "video": "https://www.youtube.com/shorts/mkNBqb51hPM", "usa_carga": False},
                        {"nome": "Deslocamento Frente e Trás", "series": 2, "reps": "Tabata", "video": "https://www.youtube.com/shorts/tGpiicrGP60", "usa_carga": False},
                        {"nome": "Mountain Climbers", "series": 2, "reps": "Tabata", "video": "https://www.youtube.com/watch?v=ruQ4ZwncXBg", "usa_carga": False}
                    ]
                }
            ],
            "Treino B": [
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Prone Db Drops", "reps": "10", "video": "https://www.instagram.com/p/C8PJClxtgYC/", "usa_carga": False},
                        {"nome": "Band Plyo Pullover [Veloz]", "reps": "8", "video": "https://www.youtube.com/shorts/5hKWgGWxu0Y", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Pull Throughs", "reps": "10", "video": "https://www.youtube.com/watch?v=ZuKowDpVVXM", "usa_carga": False},
                        {"nome": "Band Split Stance RDL", "reps": "8/8", "video": "https://www.youtube.com/watch?v=u_FgMbRXZh8", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Single Arm Rotatiion Row", "reps": "8/8", "video": "https://www.youtube.com/shorts/GdRULSXCWdk", "usa_carga": False},
                        {"nome": "Band Sumo Deadlift High Pull", "reps": "10", "video": "https://www.youtube.com/watch?v=G_YGop6nCn8", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Face Pull", "reps": "10", "video": "https://www.youtube.com/shorts/1s-0WtJMsu8", "usa_carga": False},
                        {"nome": "Glute Bridge Walkout", "reps": "10", "video": "https://www.youtube.com/watch?v=RpVJ40VGPr0", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Curls", "reps": "10", "video": "https://www.youtube.com/shorts/20xtfGZ37nw", "usa_carga": False},
                        {"nome": "Bycicle Crunch", "reps": "20", "video": "https://www.youtube.com/shorts/CakPX7X-mSw", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "conjugado",
                    "series": 3,
                    "feitas": 0,
                    "exercicios": [
                        {"nome": "Band Pallof Rotation", "reps": "8/8", "video": "https://www.youtube.com/shorts/XJkm_PU_ztQ", "usa_carga": False},
                        {"nome": "Band Broad Jump", "reps": "10", "video": "https://www.youtube.com/shorts/Wd1SoKetX2U", "usa_carga": False}
                    ]
                },
                {
                    "tipo": "titulo",
                    "texto": "💦 Cardio 2"
                },
                {
                    "tipo": "simples",
                    "exercicios": [
                        {"nome": "Aquecer 3' [Trote] + 12 Tiros 40m [Descanso 1']", "series": 1, "reps": "12 Tiros", "usa_carga": False}
                    ]
                }
            ]
        }
    }
}