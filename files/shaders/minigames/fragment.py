min_fragment = """
        #version 330 core
        uniform sampler2D image;

        out vec4 color;
        in vec2 fragmentTexCoord;

        void main()
        {
            vec2 fragCoord = fragmentTexCoord.xy;
            highp float y_pos = fragCoord.y * 100;
            
            if (mod(y_pos, 1.45) < 1)
            {
                discard;
            }
            float saturation = 0.260f;
            color = texture(image, fragmentTexCoord) - vec4(saturation, saturation, saturation, saturation) + vec4(0.15, 0.15, 0.15, 0.0);
        }
"""