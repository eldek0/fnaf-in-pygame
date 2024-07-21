fragment = """
            #version 330 core
            uniform sampler2D image;

            out vec4 color;
            in vec2 fragmentTexCoord;

            void main() {
                float dir;
                vec2 coords;
                float offset;
                float pixelDistanceX;
                float pixelDistanceY;
                
                pixelDistanceX = distance(fragmentTexCoord.x, 0.5);
                pixelDistanceY = distance(fragmentTexCoord.y, 0.5);

                offset = (pixelDistanceX * 0.1) * pixelDistanceY;

                if (fragmentTexCoord.y <= 0.5){
                    dir = 1.0;
                }
                else{
                    dir = -1.0;
                }

                coords = vec2(fragmentTexCoord.x, fragmentTexCoord.y + pixelDistanceX*(offset*8.0*dir));

                color = vec4(texture(image, coords).rgb, 1.0);
            }
"""