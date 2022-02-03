# ban-pick-flask

Ban-pick is a tool designed for [Age of Empires II: Definitive Edition](https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/). It allows you and your friend to semi-randomly select civilizations for gaming.

## Usage

- Install Dependencies

```bash
pip install -r requirements.txt
python main.py
```

- Open [http://127.0.0.1:5000](http://127.0.0.1:5000) on your browser
- Input:
  - Rand Count - the total number of civilizations available for each player  
  - Ban Count - the number of civilizations will be banned for each player
- Click **submit** button
- Click the icon of the civilizations you ban it for another player
- Click **submit** button
- The matches will be scheduled

## TODO

- Add data validation
- Improve UI
- ...

