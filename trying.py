import math
import unittest



def rgbtoangle(rgb):

  const = 60
  #used to multiplications

  rgb = abs(rgb)

  R = rgb // 1000000
  #getting r using floor division
  rgb = rgb % 1000000
  #redefining rgb to eliminate R

  G = rgb // 1000
  #getting G using floor Division

  B = rgb % 1000
  #Getting B using Modulus

  #Normalizing the RGB Values

  r, g, b = R / 255, G / 255, B / 255

  Cmax = max(r,g,b)
  #getting Max value

  Cmin = min(r, g, b)
  #getting Min Value

  #Getting Delta
  delta = Cmax - Cmin
  # print(f"CMAX --- {Cmax} CMIN -- {Cmin} R -- {r} B --{b} G -- {g}")
  if r>1 or g>1 or b>1:
    return None
  if r == 1 or g == 1 or b == 1:
    if r == 0 or g == 0 or b == 0:
      if Cmax == r:
        Hue = ( 60 * ((g - b) / delta)) % 360
        return round(Hue)
      elif Cmax == g:
        Hue = (60*((b-r) / delta) + 120) % 360
        return round(Hue)
      elif Cmin == b:
        Hue = (60 * ((r-g) / delta) + 240) % 360
        return round(Hue)
      elif Cmax == Cmin:
        return 0
    else:
      return None
  else:
    return None
  

def angletoRGB(Hue):

    H = Hue % 360
    S = 1
    V = 1


    chroma = S * V

    Inter_value = chroma * (1 - abs((H/60)%2-1))

    lightness = V - chroma

    if 0 <= H  and H < 60:
      R,G,B = chroma, Inter_value, 0
    elif 60 <= H and H < 120:
      R,G,B = Inter_value, chroma, 0
    elif 120 <= H and H < 180:
      R,G,B = 0, chroma, Inter_value
    elif 180 <= H and H < 240:
      R,G,B = 0, Inter_value, chroma
    elif 240 <= H and H < 300:
      R,G,B = Inter_value, 0, chroma
    elif 300 <= H and H < 360:
      R,G,B = chroma, 0, Inter_value

    R = round((R + lightness) * 255)
    G = round((G + lightness) * 255)
    B = round((B + lightness) * 255)

    rgb = int((R*1000000)+(G*1000)+B)

    return rgb



def colorHarmony(rgb1, rgb2):
  HUE_1 = rgbtoangle(rgb1)

  HUE_2 = rgbtoangle(rgb2)

  hue_mean = (HUE_1 + HUE_2) / 2



  return angletoRGB(hue_mean)


class TestSome(unittest.TestCase):

  def test_rgbtoangle(self):
    self.assertEqual(rgbtoangle(255000000), 0, "Should  be Zero")
    self.assertEqual(rgbtoangle(255128000), 30, "Should be 30")
    self.assertEqual(rgbtoangle(255234010), None, "Should be None")


  def test_angletorgb(self):
    self.assertEqual(angletoRGB(0), 255000000, "Should be 255000000")
    self.assertEqual(angletoRGB(360), 255000000, "Should be 255000000")
    self.assertEqual(angletoRGB(0.2), 255001000, "Should be 255001000")
    self.assertEqual(angletoRGB(30), 255128000, "Should be 255128000")

  def test_colorharmony(self):
    self.assertEqual(colorHarmony(255128000, 255128000), 255128000)
    self.assertEqual(colorHarmony(255255000, 255000000), 255128000)
    self.assertEqual(colorHarmony(255038000, 255034000), 255036000)
if __name__ == '__main__':
  unittest.main()