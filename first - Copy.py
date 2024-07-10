{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "877e47ff-b9ee-47ad-8bba-8228085cf36c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "d906bfac-eb34-4518-ba23-4a22c1dd0c75",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ucimlrepo import fetch_ucirepo \n",
    "  \n",
    "# fetch dataset \n",
    "yeast = fetch_ucirepo(id=110) \n",
    "  \n",
    "# data (as pandas dataframes) \n",
    "X = yeast.data.features \n",
    "y = yeast.data.targets\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "id": "f44574af-0dc0-4e3f-a6c1-e4b55570fd2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ucimlrepo import fetch_ucirepo \n",
    "  \n",
    "# fetch dataset \n",
    "rice_cammeo_and_osmancik = fetch_ucirepo(id=545) \n",
    "\n",
    "df = rice_cammeo_and_osmancik.data.to_data\n",
    "# data (as pandas dataframes) \n",
    "X = rice_cammeo_and_osmancik.data.features \n",
    "y = rice_cammeo_and_osmancik.data.targets \n",
    "  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "id": "e53ca521-5d4c-49ac-89e1-322999eb5596",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.concat([X,y], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "632232fb-3df9-4b54-ad8b-1f2f792a7879",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "id": "7a837f5f-93c2-4c5f-83d5-bd00ae6ee4df",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\preprocessing\\_label.py:114: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "label_encoder = LabelEncoder()\n",
    "y_encoded = label_encoder.fit_transform(y)\n",
    "\n",
    "# Split data into train and test sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "id": "0d68b979-9ac3-41a6-b0b8-2b6e0e75233c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import mean_squared_error, accuracy_score\n",
    "\n",
    "# Split data into train and test sets\n",
    "# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 298,
   "id": "a191684a-72f7-4ab0-833c-d3cd9f4c853e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Forest Accuracy: 0.6363636363636364\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "# Train the model\n",
    "rf_clf = RandomForestClassifier(random_state=93)\n",
    "rf_clf.fit(X_train, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred_rf = rf_clf.predict(X_test)\n",
    "\n",
    "# Evaluate the model\n",
    "accuracy_rf = accuracy_score(y_test, y_pred_rf)\n",
    "print(f'Random Forest Accuracy: {accuracy_rf}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 299,
   "id": "f2105dbf-524b-443b-950b-fc8a19c46503",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " MSE: 11.282828282828282,    Accuracy: 0.6363636363636364\n"
     ]
    }
   ],
   "source": [
    "# Evaluate the model\n",
    "mse_rf = mean_squared_error(y_test, y_pred_rf)\n",
    "accuracy_rf = accuracy_score(y_test, y_pred_rf)\n",
    "print(f' MSE: {mse_rf},    Accuracy: {accuracy_rf}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a00de45c-1239-488f-b9f1-a2cd4afc1278",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "34b858a3-f105-4d31-bfd4-925db474e0bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "XGBoost Accuracy: 0.9186351706036745\n"
     ]
    }
   ],
   "source": [
    "import xgboost as xgb         # for rice\n",
    "\n",
    "# Train the model\n",
    "xgb_clf = xgb.XGBClassifier()\n",
    "xgb_clf.fit(X_train, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred_xgb = xgb_clf.predict(X_test)\n",
    "\n",
    "# Evaluate the model\n",
    "accuracy_xgb = accuracy_score(y_test, y_pred_xgb)\n",
    "print(f'XGBoost Accuracy: {accuracy_xgb}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "73be2801-24f7-489c-8e4a-e32dc85c22c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "N = df.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "id": "46000710-fe90-4c82-8d61-a25514042d65",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], N, p=[1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "id": "0ed32250-9236-4e8c-ba68-8f9f1d5003c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "id": "38caaaa1-765b-4668-8ebf-4644c8cc8cae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mcg</th>\n",
       "      <th>gvh</th>\n",
       "      <th>alm</th>\n",
       "      <th>mit</th>\n",
       "      <th>erl</th>\n",
       "      <th>pox</th>\n",
       "      <th>vac</th>\n",
       "      <th>nuc</th>\n",
       "      <th>localization_site</th>\n",
       "      <th>random</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.58</td>\n",
       "      <td>0.61</td>\n",
       "      <td>0.47</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.48</td>\n",
       "      <td>0.22</td>\n",
       "      <td>MIT</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.43</td>\n",
       "      <td>0.67</td>\n",
       "      <td>0.48</td>\n",
       "      <td>0.27</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.22</td>\n",
       "      <td>MIT</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.64</td>\n",
       "      <td>0.62</td>\n",
       "      <td>0.49</td>\n",
       "      <td>0.15</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.22</td>\n",
       "      <td>MIT</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.58</td>\n",
       "      <td>0.44</td>\n",
       "      <td>0.57</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.54</td>\n",
       "      <td>0.22</td>\n",
       "      <td>NUC</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.42</td>\n",
       "      <td>0.44</td>\n",
       "      <td>0.48</td>\n",
       "      <td>0.54</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.48</td>\n",
       "      <td>0.22</td>\n",
       "      <td>MIT</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1479</th>\n",
       "      <td>0.81</td>\n",
       "      <td>0.62</td>\n",
       "      <td>0.43</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.22</td>\n",
       "      <td>ME2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1480</th>\n",
       "      <td>0.47</td>\n",
       "      <td>0.43</td>\n",
       "      <td>0.61</td>\n",
       "      <td>0.40</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.48</td>\n",
       "      <td>0.47</td>\n",
       "      <td>NUC</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1481</th>\n",
       "      <td>0.67</td>\n",
       "      <td>0.57</td>\n",
       "      <td>0.36</td>\n",
       "      <td>0.19</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.56</td>\n",
       "      <td>0.22</td>\n",
       "      <td>ME2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1482</th>\n",
       "      <td>0.43</td>\n",
       "      <td>0.40</td>\n",
       "      <td>0.60</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.39</td>\n",
       "      <td>NUC</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1483</th>\n",
       "      <td>0.65</td>\n",
       "      <td>0.54</td>\n",
       "      <td>0.54</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.22</td>\n",
       "      <td>CYT</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1484 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       mcg   gvh   alm   mit  erl  pox   vac   nuc localization_site  random\n",
       "0     0.58  0.61  0.47  0.13  0.5  0.0  0.48  0.22               MIT       1\n",
       "1     0.43  0.67  0.48  0.27  0.5  0.0  0.53  0.22               MIT       2\n",
       "2     0.64  0.62  0.49  0.15  0.5  0.0  0.53  0.22               MIT       4\n",
       "3     0.58  0.44  0.57  0.13  0.5  0.0  0.54  0.22               NUC       5\n",
       "4     0.42  0.44  0.48  0.54  0.5  0.0  0.48  0.22               MIT       2\n",
       "...    ...   ...   ...   ...  ...  ...   ...   ...               ...     ...\n",
       "1479  0.81  0.62  0.43  0.17  0.5  0.0  0.53  0.22               ME2       5\n",
       "1480  0.47  0.43  0.61  0.40  0.5  0.0  0.48  0.47               NUC       3\n",
       "1481  0.67  0.57  0.36  0.19  0.5  0.0  0.56  0.22               ME2       3\n",
       "1482  0.43  0.40  0.60  0.16  0.5  0.0  0.53  0.39               NUC       5\n",
       "1483  0.65  0.54  0.54  0.13  0.5  0.0  0.53  0.22               CYT       5\n",
       "\n",
       "[1484 rows x 10 columns]"
      ]
     },
     "execution_count": 306,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66355d2e-76bd-4dc5-a079-3dcb1db0e751",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for rice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "4c5ef3d3-00b2-4b61-a138-1cfde1edda71",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "index = df[df[\"random\"]==10].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"Area\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "549bebe2-8d10-44c0-816d-5241ff2a04f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "index = df[df[\"random\"]==9].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"Area\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "496e653e-0ec4-4fb9-ac1d-8f8c68d509be",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for yeast"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 307,
   "id": "2b939eeb-dceb-46e0-a198-57a3ea1e0d4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"mcg\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 308,
   "id": "7ded5a4b-c946-4ebc-b3fa-07daaff98abc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"gvh\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 309,
   "id": "9efe3784-6885-44d5-9c6d-8060661f50a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"alm\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 310,
   "id": "e5b36909-1357-4d93-a4fa-f583b4eb340c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"mit\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "id": "fb3df606-f45c-46d3-97d1-eeebac7587cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"erl\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "id": "4dcfab19-4bb8-4b5b-95b4-ae9e7b450dda",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"vac\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 313,
   "id": "e6bf7609-9c02-4864-9fba-d8af02ab1d27",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"random\"] = np.random.choice([1, 2, 3, 4, 5], N, p=[1/5, 1/5, 1/5, 1/5, 1/5])\n",
    "index = df[df[\"random\"]==5].index\n",
    "# Replace with NaN\n",
    "df.loc[index,\"nuc\"] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fccdb4a1-bae2-4950-be5f-a18d0f23bed1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5347009-91f1-483b-8d00-9a6285979aec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "0a384fe3-09a3-42b7-8c15-a99dcdcf56af",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for Rice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "4ec8d884-340c-4014-9fa8-37537504f688",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "749"
      ]
     },
     "execution_count": 236,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Area.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "id": "848f8c0b-884a-4c0e-addb-6430cb6e9c6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       15231.0\n",
       "1       14656.0\n",
       "2           NaN\n",
       "3       13176.0\n",
       "4       14688.0\n",
       "         ...   \n",
       "3805    11441.0\n",
       "3806    11625.0\n",
       "3807    12437.0\n",
       "3808     9882.0\n",
       "3809        NaN\n",
       "Name: Area, Length: 3810, dtype: float64"
      ]
     },
     "execution_count": 237,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Area"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fdf0c6f-566d-4a0c-ba8a-38086d1faf0f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "4d534aab-ec82-4010-8f15-350264b86858",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for yesast"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7252060-9b41-4b68-9552-2914adaec029",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "id": "f84c805f-3dbe-4728-81a9-d3afa836fade",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "301"
      ]
     },
     "execution_count": 314,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.mcg.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "id": "ba4c147d-8c4c-4c09-a0cc-db737f00def5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "326"
      ]
     },
     "execution_count": 315,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.gvh.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "id": "0aa2dc48-0b75-4cf4-ac62-de1704cbdc3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       0.61\n",
       "1       0.67\n",
       "2       0.62\n",
       "3       0.44\n",
       "4        NaN\n",
       "        ... \n",
       "1479    0.62\n",
       "1480    0.43\n",
       "1481    0.57\n",
       "1482    0.40\n",
       "1483     NaN\n",
       "Name: gvh, Length: 1484, dtype: float64"
      ]
     },
     "execution_count": 316,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.gvh"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f6e6afe-6e19-4539-af13-25c0d415a4d9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b021a813-6d55-4ed0-96c4-0b289cc48096",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cf9da2b-a27a-4a26-ae70-91c977698063",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbc2e838-23f6-4fec-9cce-af7b0dfc8de1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "229f9d4f-1f7d-4e15-9be0-59ba9fc1a386",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       0.58\n",
       "1       0.43\n",
       "2       0.50\n",
       "3       0.58\n",
       "4       0.42\n",
       "        ... \n",
       "1479    0.81\n",
       "1480    0.47\n",
       "1481    0.50\n",
       "1482    0.43\n",
       "1483    0.65\n",
       "Name: mcg, Length: 1484, dtype: float64"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "6424c029-f4ae-40da-9747-9c1cfd62ccfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mcg\n",
       "0.50    349\n",
       "0.45     44\n",
       "0.48     44\n",
       "0.51     42\n",
       "0.49     42\n",
       "       ... \n",
       "0.95      1\n",
       "0.97      1\n",
       "1.00      1\n",
       "0.22      1\n",
       "0.92      1\n",
       "Name: count, Length: 78, dtype: int64"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.mcg.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "670588c5-96a3-4d30-83d7-ef176aa9e96a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       0.61\n",
       "1       0.67\n",
       "2       0.62\n",
       "3       0.44\n",
       "4       0.44\n",
       "        ... \n",
       "1479    0.62\n",
       "1480    0.43\n",
       "1481    0.57\n",
       "1482    0.40\n",
       "1483    0.54\n",
       "Name: gvh, Length: 1484, dtype: float64"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc619b7a-4fcc-4d39-be3a-bd474f744607",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "0b8da119-f061-4bd4-9c09-ed7c9497c64b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for rice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "id": "9178aa5f-d954-49e1-b3e4-c8bcbf290943",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df[[\"Area\", \"Perimeter\" , \"Major_Axis_Length\" , \"Minor_Axis_Length\", \"Eccentricity\", \"Convex_Area\", \"Extent\"]]\n",
    "y = df[[\"Class\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "810b88e4-29cd-4baa-bd24-6e4b797060c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for yeast"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "id": "56b2a32a-4923-4b10-baaa-dae035102b3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df[['mcg', 'gvh' , 'alm' , 'mit', 'erl', 'vac', 'nuc']]\n",
    "y = df[['localization_site']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "id": "5ccb94e3-9579-4361-8886-09873cb83984",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "301"
      ]
     },
     "execution_count": 318,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.mcg.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbcb466b-fcc5-4a83-9a89-780f151d1fdc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "855cbb77-42ca-4031-ba54-ec8139dd425e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "503437e3-94bf-4729-b0ac-75d50de465d8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "id": "c4c7c4d5-5414-4515-87d3-0c5d74acfa57",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\preprocessing\\_label.py:114: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "label_encoder = LabelEncoder()\n",
    "y_encoded = label_encoder.fit_transform(y)\n",
    "\n",
    "# Split data into train and test sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=201773407)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "id": "63af307d-d9b2-4010-8b0c-880c56f48f5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "62"
      ]
     },
     "execution_count": 320,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.mcg.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "id": "c38283fc-740f-4cf0-9818-f5484faebac6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "563     0.32\n",
       "435     0.44\n",
       "1214    0.43\n",
       "257     0.42\n",
       "319     0.69\n",
       "        ... \n",
       "33      0.33\n",
       "842      NaN\n",
       "170     0.31\n",
       "10      0.43\n",
       "1073     NaN\n",
       "Name: mcg, Length: 297, dtype: float64"
      ]
     },
     "execution_count": 325,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.mcg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15331272-a8fd-4b4d-989a-78d2cd116477",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "mean_train_data = X_train.mcg.mean()\n",
    "X_train.mcg = X_train.mcg.fillna(mean_train_data).round(2)\n",
    "X_test.mcg = X_test.mcg.fillna(mean_train_data).round(2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "id": "8cf2e2e0-610b-4b12-920d-eb6a45994b3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mcg    0.501382\n",
       "gvh    0.500474\n",
       "alm    0.502305\n",
       "mit    0.263316\n",
       "erl    0.505820\n",
       "vac    0.499696\n",
       "nuc    0.278246\n",
       "dtype: float64"
      ]
     },
     "execution_count": 329,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.mean(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "id": "ce8eddd5-7a53-4048-aa04-1ad8e43edae2",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "X_train= X_train.fillna(X_train.mean()).round(2)\n",
    "X_test = X_test.fillna(X_train.mean()).round(2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
   "id": "8a60eae1-9fdb-4c30-9380-b361fe24044a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "563     0.32\n",
       "435     0.44\n",
       "1214    0.43\n",
       "257     0.42\n",
       "319     0.69\n",
       "        ... \n",
       "33      0.33\n",
       "842     0.50\n",
       "170     0.31\n",
       "10      0.43\n",
       "1073    0.50\n",
       "Name: mcg, Length: 297, dtype: float64"
      ]
     },
     "execution_count": 332,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.mcg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "id": "c73f6e51-a28d-480d-a09d-4ca8e0975751",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 333,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.mcg.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "369ee525-ff5c-4472-85bf-262c0f84ae59",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for rice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "id": "028f8009-f71a-496e-9924-23f482b5bd4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "151"
      ]
     },
     "execution_count": 241,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.Area.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "8dcb22b6-866d-48c8-b82d-4fb2267c1a78",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_train_data = X_train.Area.mean()\n",
    "X_train.Area = X_train.Area.fillna(mean_train_data).round(2)\n",
    "X_test.Area = X_test.Area.fillna(mean_train_data).round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "8c023ed8-214b-468b-955e-835e981f942c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 243,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.Area.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ceb91314-9676-46d6-a27e-2f4af62f3f72",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 334,
   "id": "70ed9d6c-8e25-48ce-8b5f-4bfa2393fed5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " MSE: 16.986531986531986,    Accuracy: 0.4781144781144781\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "# Train the model\n",
    "rf_clf = RandomForestClassifier(random_state=201773407)\n",
    "rf_clf.fit(X_train, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred_rf = rf_clf.predict(X_test)\n",
    "# Evaluate the model\n",
    "mse_rf = mean_squared_error(y_test, y_pred_rf)\n",
    "accuracy_rf = accuracy_score(y_test, y_pred_rf)\n",
    "print(f' MSE: {mse_rf},    Accuracy: {accuracy_rf}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7cd803d-c9e7-4a77-b6af-0e3955b853c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "id": "f237a21a-30e0-44b1-98a5-0e0099dba07e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "XGBoost Accuracy: 0.5454545454545454\n"
     ]
    }
   ],
   "source": [
    "import xgboost as xgb         # for rice\n",
    "\n",
    "# Train the model\n",
    "xgb_clf = xgb.XGBClassifier()\n",
    "xgb_clf.fit(X_train, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred_xgb = xgb_clf.predict(X_test)\n",
    "\n",
    "# Evaluate the model\n",
    "accuracy_xgb = accuracy_score(y_test, y_pred_xgb)\n",
    "print(f'XGBoost Accuracy: {accuracy_xgb}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f8c2f7c-4f89-4bd8-b742-fe9bb408e19b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8f4361d-2118-4df8-9bab-1cec8ce4e741",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22359ff3-5b4e-4c2b-b4d1-2446eeda27a8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8887cc7-4120-4f36-8550-20d5919b6e4b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 340,
   "id": "34b49016-0415-4164-856d-836d249390d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n",
      "C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\model_selection\\_split.py:737: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best k value: 7 with accuracy: 0.5400808424635677\n"
     ]
    }
   ],
   "source": [
    "from sklearn.impute import KNNImputer\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import train_test_split, cross_val_score\n",
    "\n",
    "# Define a function to evaluate different k values\n",
    "def evaluate_knn_imputation(k_values, X, y):\n",
    "    results = {}\n",
    "    for k in k_values:\n",
    "        knn_imputer = KNNImputer(n_neighbors=k)\n",
    "        X_imputed = knn_imputer.fit_transform(X)\n",
    "        \n",
    "        # Split the data into training and testing sets\n",
    "        X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=1)\n",
    "        \n",
    "        # Train and evaluate a model (e.g., Random Forest) on the imputed data\n",
    "        rf_clf = RandomForestClassifier(random_state=201773407)\n",
    "        rf_clf.fit(X_train, y_train)\n",
    "        \n",
    "        # Evaluate the model using cross-validation\n",
    "        scores = cross_val_score(rf_clf, X_train, y_train, cv=5, scoring='accuracy')\n",
    "        results[k] = scores.mean()\n",
    "    return results\n",
    "\n",
    "# Evaluate different k values\n",
    "k_values = range(1, 21)\n",
    "results = evaluate_knn_imputation(k_values, X, y_encoded)\n",
    "\n",
    "# Find the best k value\n",
    "best_k = max(results, key=results.get)\n",
    "print(f'Best k value: {best_k} with accuracy: {results[best_k]}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4c577c6-23b8-4cbb-88ef-cf070f97386b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 341,
   "id": "40a9b4fe-61ed-4ba3-886e-b2ffb69e550e",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "acc = [83.64, 67.81,74]\n",
    "name = [\"Complete Data\", \"Mean Imputation\", \"KNN Imputation\"]\n",
    "\n",
    "g = pd.DataFrame({\"Type\":name, \"Accuracy\": acc})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 342,
   "id": "16aec44c-f72e-42ca-a0e5-97915a0ff1b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Type</th>\n",
       "      <th>Accuracy</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Complete Data</td>\n",
       "      <td>83.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mean Imputation</td>\n",
       "      <td>67.81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>KNN Imputation</td>\n",
       "      <td>74.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Type  Accuracy\n",
       "0    Complete Data     83.64\n",
       "1  Mean Imputation     67.81\n",
       "2   KNN Imputation     74.00"
      ]
     },
     "execution_count": 342,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "id": "b22ad605-d504-41c7-8427-da034f457a9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 353,
   "id": "c62250d6-0efe-461c-b424-e04de971077e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhMAAAGJCAYAAAAwtrGcAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAABQjUlEQVR4nO3deVxN+f8H8NdtUWm5Ka3clLUkRIYwDBoJyciSNTQYwrdso/mOdYbK2Gn48qUskWUwlsEQMpaSdcZYi5RRESqKos7vD7/O11XR7d7c8Ho+HvfB/ZzP+Zz3vY7bq889i0QQBAFERERE5aSh7gKIiIjow8YwQUREREphmCAiIiKlMEwQERGRUhgmiIiISCkME0RERKQUhgkiIiJSCsMEERERKYVhgoiIiJTCMEH0nkkkEsycOVPh9ZKSkiCRSBAREaHymkjesWPHIJFIsH37dnWXQvRBYJigT1JERAQkEgkkEglOnDhRbLkgCJDJZJBIJOjevbsaKlSN3377DRKJBNbW1igsLFR3OfT/ioJhWR5JSUnqLpfonbTUXQCROunq6mLTpk1o27atXHtMTAzu3r0LHR0dNVWmGpGRkbC1tUVSUhKOHDkCNzc3dZdEAMzMzLBhwwa5tgULFuDu3btYtGhRsb5ElR3DBH3Sunbtim3btmHp0qXQ0vrff4dNmzahefPmyMjIUGN1ysnJycGvv/6K4OBghIeHIzIystKGiZycHOjr66u7jPdGX18fgwYNkmuLiorC48ePi7UTfQj4NQd90vr374+HDx/i0KFDYlt+fj62b9+OAQMGlLhOTk4OJk6cCJlMBh0dHTRo0ADz58/HmzfgzcvLQ2BgIMzMzGBoaIgePXrg7t27JY75zz//YPjw4bCwsICOjg4cHR2xdu1apV7bzp078ezZM/Tp0wc+Pj7YsWMHnj9/Xqzf8+fPMXPmTNSvXx+6urqwsrJCr169kJiYKPYpLCzEkiVL4OTkBF1dXZiZmaFLly44e/YsgLcfz/HmMSIzZ86ERCLBlStXMGDAAFSrVk2cGfrzzz8xdOhQ1K5dG7q6urC0tMTw4cPx8OHDEt8zPz8/WFtbQ0dHB3Z2dhg9ejTy8/Nx69YtSCSSYr/lA8CpU6cgkUiwefPmd76HBQUF+O6772BpaQl9fX306NEDKSkp4vIZM2ZAW1sbDx48KLbuyJEjYWxsXOJ7Xhbt27dHkyZNSlzWoEEDuLu7A/jfez9//nwsWrQItWrVgp6eHtq3b4/Lly8XW/fatWvo3bs3TExMoKurCxcXF+zevbtcNRIVYZigT5qtrS1cXV3lfrDs378fWVlZ8PHxKdZfEAT06NEDixYtQpcuXbBw4UI0aNAAkydPxoQJE+T6fv3111i8eDE6d+6MkJAQaGtro1u3bsXGTE9PR6tWrXD48GGMHTsWS5YsQd26deHn54fFixeX+7VFRkaiQ4cOsLS0hI+PD548eYI9e/bI9SkoKED37t0xa9YsNG/eHAsWLMC//vUvZGVlyf0g8vPzQ0BAAGQyGUJDQzF16lTo6uoiNja23PX16dMHubm5mDt3LkaMGAEAOHToEG7duoVhw4Zh2bJl8PHxQVRUFLp27SoX1u7du4fPPvsMUVFR6NevH5YuXYrBgwcjJiYGubm5qF27Ntq0aYPIyMgS3xdDQ0N4eXm9s8Y5c+Zg3759+PbbbzF+/HgcOnQIbm5uePbsGQBg8ODBePnyJbZs2SK3XlEg9fb2hq6ubrnen8GDB+PPP/8sFgji4+Nx48aNYjMY69evx9KlS+Hv74+goCBcvnwZHTt2RHp6utjn77//RqtWrXD16lVMnToVCxYsgL6+Pnr27ImdO3eWq04iAIBA9AkKDw8XAAjx8fHC8uXLBUNDQyE3N1cQBEHo06eP0KFDB0EQBKFWrVpCt27dxPV27dolABB+/PFHufF69+4tSCQSISEhQRAEQbh48aIAQBgzZoxcvwEDBggAhBkzZohtfn5+gpWVlZCRkSHX18fHR5BKpWJdt2/fFgAI4eHh73x96enpgpaWlrB69WqxrXXr1oKXl5dcv7Vr1woAhIULFxYbo7CwUBAEQThy5IgAQBg/fnypfd5W25uvd8aMGQIAoX///sX6Fr3W123evFkAIBw/flxsGzJkiKChoSHEx8eXWtN//vMfAYBw9epVcVl+fr5QvXp1wdfXt9h6rzt69KgAQKhRo4aQnZ0ttm/dulUAICxZskRsc3V1FVq2bCm3/o4dOwQAwtGjR9+6ndd169ZNqFWrlvg8MzNT0NXVFb799lu5fuPHjxf09fWFp0+fCoLwv/deT09PuHv3rtgvLi5OACAEBgaKbZ06dRKcnJyE58+fi22FhYVC69athXr16pW5VqI3cWaCPnl9+/bFs2fPsHfvXjx58gR79+4t9SuO3377DZqamhg/frxc+8SJEyEIAvbv3y/2A1CsX0BAgNxzQRDwyy+/wNPTE4IgICMjQ3y4u7sjKysL58+fV/g1RUVFQUNDA97e3mJb//79sX//fjx+/Fhs++WXX1C9enWMGzeu2BgSiUTsI5FIMGPGjFL7lMc333xTrE1PT0/8+/Pnz5GRkYFWrVoBgPg+FBYWYteuXfD09ISLi0upNfXt2xe6urpysxMHDx5ERkZGmY9LGDJkCAwNDcXnvXv3hpWVlfjvW9QnLi5O7muhyMhIyGQytG/fvkzbKYlUKoWXlxc2b94szsoUFBRgy5Yt6NmzZ7FjTHr27IkaNWqIzz/77DO0bNlSrPXRo0c4cuQI+vbtiydPnoj72cOHD+Hu7o6bN2/in3/+KXe99GljmKBPnpmZGdzc3LBp0ybs2LEDBQUF6N27d4l979y5A2tra7kfMADg4OAgLi/6U0NDA3Xq1JHr16BBA7nnDx48QGZmJlatWgUzMzO5x7BhwwAA9+/fV/g1bdy4EZ999hkePnyIhIQEJCQkwNnZGfn5+di2bZvYLzExEQ0aNJA7+PRNiYmJsLa2homJicJ1vI2dnV2xtkePHuFf//oXLCwsoKenBzMzM7FfVlYWgFfvWXZ2Nho1avTW8Y2NjeHp6YlNmzaJbZGRkahRowY6duxYphrr1asn91wikaBu3bpyp2v269cPOjo6YmjJysrC3r17MXDgQKXCFvAqqCQnJ+OPP/4AABw+fBjp6ekYPHjwO2sFgPr164u1JiQkQBAETJs2rdi+VhQUy7OvEQE8m4MIADBgwACMGDECaWlp8PDwgLGx8XvZbtG1HwYNGgRfX98S+zRu3FihMW/evIn4+HgAJf+AiYyMxMiRIxWs9O1K+6FZUFBQ6jqvz0IU6du3L06dOoXJkyejadOmMDAwQGFhIbp06VKu62QMGTIE27Ztw6lTp+Dk5ITdu3djzJgx0NBQ3e9R1apVQ/fu3REZGYnp06dj+/btyMvLU8lZGe7u7rCwsMDGjRvRrl07bNy4EZaWluU6K6fo/Zs0aZJ48Oab6tatq1S99OlimCAC8NVXX2HUqFGIjY0tdjDd62rVqoXDhw/jyZMncrMT165dE5cX/VlYWCj+5l/k+vXrcuMVnelRUFCgstM2IyMjoa2tjQ0bNkBTU1Nu2YkTJ7B06VIkJyfDxsYGderUQVxcHF68eAFtbe0Sx6tTpw4OHjyIR48elTo7Ua1aNQBAZmamXHvRTE1ZPH78GNHR0Zg1axamT58utt+8eVOun5mZGYyMjEo8U+FNXbp0gZmZGSIjI9GyZUvk5uaW+Ft9ad7ctiAISEhIKBbwhgwZAi8vL8THxyMyMhLOzs5wdHQs83ZKo6mpiQEDBiAiIgKhoaHYtWsXRowYUezftaRaAeDGjRuwtbUFANSuXRsAoK2tXWlPEaYPF7/mIAJgYGCAFStWYObMmfD09Cy1X9euXVFQUIDly5fLtS9atAgSiQQeHh4AIP65dOlSuX5vnp2hqakJb29v/PLLLyX+cCzplMN3iYyMxOeff45+/fqhd+/eco/JkycDgHj2ire3NzIyMoq9HgDi9/Te3t4QBAGzZs0qtY+RkRGqV6+O48ePyy3/+eefy1x30Q9I4Y1TbN98zzQ0NNCzZ0/s2bNHPDW1pJoAQEtLC/3798fWrVsREREBJycnhWZ61q9fjydPnojPt2/fjtTUVPHft4iHhweqV6+O0NBQxMTEqPRaEYMHD8bjx48xatQoPH36tNSxd+3aJXfMw5kzZxAXFyfWam5uji+++AL/+c9/kJqaWmz98uxrREU4M0H0/0r7muF1np6e6NChA/79738jKSkJTZo0we+//45ff/0VAQEB4jESTZs2Rf/+/fHzzz8jKysLrVu3RnR0NBISEoqNGRISgqNHj6Jly5YYMWIEGjZsiEePHuH8+fM4fPgwHj16VObXEBcXh4SEBIwdO7bE5TVq1ECzZs0QGRmJb7/9FkOGDMH69esxYcIEnDlzBp9//jlycnJw+PBhjBkzBl5eXujQoQMGDx6MpUuX4ubNm+JXDn/88Qc6dOggbuvrr79GSEgIvv76a7i4uOD48eO4ceNGmWs3MjJCu3btMG/ePLx48QI1atTA77//jtu3bxfrO3fuXPz+++9o3749Ro4cCQcHB6SmpmLbtm04ceKE3NdUQ4YMwdKlS3H06FGEhoaWuR4AMDExQdu2bTFs2DCkp6dj8eLFqFu3rngqaxFtbW34+Phg+fLl0NTURP/+/RXazts4OzujUaNG2LZtGxwcHNCsWbMS+9WtWxdt27bF6NGjkZeXh8WLF8PU1BRTpkwR+4SFhaFt27ZwcnLCiBEjULt2baSnp+P06dO4e/cuLl26pLK66ROjprNIiNTq9VND3+bNU0MFQRCePHkiBAYGCtbW1oK2trZQr1494aeffhJPSSzy7NkzYfz48YKpqamgr68veHp6CikpKcVOlRSEV6dy+vv7CzKZTNDW1hYsLS2FTp06CatWrRL7lOXU0HHjxgkAhMTExFL7zJw5UwAgXLp0SRCEV6dj/vvf/xbs7OzEbffu3VtujJcvXwo//fSTYG9vL1SpUkUwMzMTPDw8hHPnzol9cnNzBT8/P0EqlQqGhoZC3759hfv375d6auiDBw+K1Xb37l3hq6++EoyNjQWpVCr06dNHuHfvXonv2Z07d4QhQ4YIZmZmgo6OjlC7dm3B399fyMvLKzauo6OjoKGhIXfq5NsUnRq6efNmISgoSDA3Nxf09PSEbt26CXfu3ClxnTNnzggAhM6dO5dpG29689TQ182bN08AIMydO7fYsqL94qeffhIWLFggyGQyQUdHR/j888/Ff+PXJSYmCkOGDBEsLS0FbW1toUaNGkL37t2F7du3l6tuIkEQBIkgvDGnSET0kXF2doaJiQmio6MrbBuXLl1C06ZNsX79eoWOyyiLJUuWIDAwEElJSbCxsZFblpSUBDs7O/z000+YNGmSSrdLVFY8ZoKIPmpnz57FxYsXMWTIkArdzurVq2FgYIBevXqpdFxBELBmzRq0b9++WJAgqix4zAQRfZQuX76Mc+fOYcGCBbCyskK/fv0qZDt79uzBlStXsGrVKowdO1ZlNyzLycnB7t27cfToUfz111/49ddfVTIuUUVgmCCij9L27dsxe/ZsNGjQAJs3by73PTLeZdy4cUhPT0fXrl1LPOOlvB48eIABAwbA2NgY3333HXr06KGysYlUjcdMEBERkVJ4zAQREREphWGCiIiIlPLRHzNRWFiIe/fuwdDQUOmb7hAREX1KBEHAkydPYG1t/dZ72nz0YeLevXuQyWTqLoOIiOiDlZKSgpo1a5a6/KMPE0U3Y0pJSYGRkZGaqyEiIvpwZGdnQyaTyd3YsETqvPzm+5CVlSUAELKystRdilq8fPlS+P777wVbW1tBV1dXqF27tjB79my5Sz/PmDFDaNCggVC1alXB2NhY6NSpkxAbG/vOse/evSsMHDhQMDExEXR1dYVGjRqVennqUaNGCQCERYsWqeqlERFRBSvrz9CPfmbiUxcaGooVK1Zg3bp1cHR0xNmzZzFs2DBIpVKMHz8eAFC/fn0sX74ctWvXxrNnz7Bo0SJ07twZCQkJMDMzK3Hcx48fo02bNujQoQP2798PMzMz3Lx5U7wV9et27tyJ2NhYWFtbV+hrJSIi9fjorzORnZ0NqVSKrKysT/Jrju7du8PCwgJr1qwR27y9vaGnp4eNGzeWuE7Re3b48GF06tSpxD5Tp07FyZMn8ccff7x1+//88w9atmyJgwcPolu3bggICEBAQEC5Xw8REb0/Zf0ZylNDP3JFt74uuhX0pUuXcOLECXh4eJTYPz8/H6tWrYJUKkWTJk1KHXf37t1wcXFBnz59YG5uDmdnZ6xevVquT2FhIQYPHozJkyfD0dFRdS+KiIgqFX7N8ZGbOnUqsrOzYW9vD01NTRQUFGDOnDkYOHCgXL+9e/fCx8cHubm5sLKywqFDh1C9evVSx7116xZWrFiBCRMm4LvvvkN8fDzGjx+PKlWqwNfXF8Crr1i0tLTEr1OIiOjjxDDxkdu6dSsiIyOxadMmODo64uLFiwgICIC1tbX4Qx8AOnTogIsXLyIjIwOrV69G3759ERcXB3Nz8xLHLSwshIuLC+bOnQvg1S2eL1++jJUrV8LX1xfnzp3DkiVLcP78eV7fg4joI8evOT5ykydPxtSpU+Hj4wMnJycMHjwYgYGBCA4Oluunr6+PunXrolWrVlizZg20tLTkjrN4k5WVFRo2bCjX5uDggOTkZADAH3/8gfv378PGxgZaWlrQ0tLCnTt3MHHiRNja2qr8dRIRkfpwZuIjl5ubW+yqZZqamigsLHzreoWFhcjLyyt1eZs2bXD9+nW5ths3bqBWrVoAgMGDB8PNzU1uubu7OwYPHoxhw4Yp8hKIiKiSY5j4yHl6emLOnDmwsbGBo6MjLly4gIULF2L48OEAgJycHMyZMwc9evSAlZUVMjIyEBYWhn/++Qd9+vQRx+nUqRO++uorjB07FgAQGBiI1q1bY+7cuejbty/OnDmDVatWYdWqVQAAU1NTmJqaytWira0NS0tLNGjQ4D29eiIieh8YJj5yy5Ytw7Rp0zBmzBjcv38f1tbWGDVqFKZPnw7g1SzFtWvXsG7dOmRkZMDU1BQtWrTAH3/8IXcGRmJiIjIyMsTnLVq0wM6dOxEUFITZs2fDzs4OixcvLnZgJxERffx4nQkiIiIqEa8zQURERO8Fv+YoJ9up+9RdAlWwpJBu6i6BiOiDwJkJIiIiUgrDBBERESmFYYKIiIiUwjBBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBS1homCggJMmzYNdnZ20NPTQ506dfDDDz/g9St8C4KA6dOnw8rKCnp6enBzc8PNmzfVWDURERG9Tq1hIjQ0FCtWrMDy5ctx9epVhIaGYt68eVi2bJnYZ968eVi6dClWrlyJuLg46Ovrw93dHc+fP1dj5URERFRErZfTPnXqFLy8vNCt26vLFtva2mLz5s04c+YMgFezEosXL8b3338PLy8vAMD69ethYWGBXbt2wcfHR221ExER0StqnZlo3bo1oqOjcePGDQDApUuXcOLECXh4eAAAbt++jbS0NLi5uYnrSKVStGzZEqdPny5xzLy8PGRnZ8s9iIiIqOKodWZi6tSpyM7Ohr29PTQ1NVFQUIA5c+Zg4MCBAIC0tDQAgIWFhdx6FhYW4rI3BQcHY9asWRVbOBEREYnUOjOxdetWREZGYtOmTTh//jzWrVuH+fPnY926deUeMygoCFlZWeIjJSVFhRUTERHRm9Q6MzF58mRMnTpVPPbByckJd+7cQXBwMHx9fWFpaQkASE9Ph5WVlbheeno6mjZtWuKYOjo60NHRqfDaiYiI6BW1zkzk5uZCQ0O+BE1NTRQWFgIA7OzsYGlpiejoaHF5dnY24uLi4Orq+l5rJSIiopKpdWbC09MTc+bMgY2NDRwdHXHhwgUsXLgQw4cPBwBIJBIEBATgxx9/RL169WBnZ4dp06bB2toaPXv2VGfpRERE9P/UGiaWLVuGadOmYcyYMbh//z6sra0xatQoTJ8+XewzZcoU5OTkYOTIkcjMzETbtm1x4MAB6OrqqrFyIiIiKiIRXr/c5EcoOzsbUqkUWVlZMDIyUtm4tlP3qWwsqpySQrqpuwQiIrUq689Q3puDiIiIlMIwQUREREphmCAiokrF1tYWEomk2MPf31+unyAI8PDwgEQiwa5du946ZlluGvno0SMMHDgQRkZGMDY2hp+fH54+farql/dRYpggIqJKJT4+HqmpqeLj0KFDAIA+ffrI9Vu8eDEkEkmZxizLTSMHDhyIv//+G4cOHcLevXtx/PhxjBw5UnUv7COm1rM5iIiI3mRmZib3PCQkBHXq1EH79u3FtosXL2LBggU4e/as3EUNS1KWm0ZevXoVBw4cQHx8PFxcXAC8OuOwa9eumD9/PqytrVX8Kj8unJkgIqJKKz8/Hxs3bsTw4cPFWYjc3FwMGDAAYWFh4pWS36YsN408ffo0jI2NxSABAG5ubtDQ0EBcXJyKX9XHh2GCiIgqrV27diEzMxNDhw4V2wIDA9G6dWtxluFdynLTyLS0NJibm8st19LSgomJSak3lqT/4dccRERUaa1ZswYeHh7i1wy7d+/GkSNHcOHCBTVXRq/jzAQREVVKd+7cweHDh/H111+LbUeOHEFiYiKMjY2hpaUFLa1XvxN7e3vjiy++KHGc128a+br09HRxmaWlJe7fvy+3/OXLl3j06FGZvkr51DFMEBFRpRQeHg5zc3N06/a/q9FOnToVf/75Jy5evCg+AGDRokUIDw8vcZyy3DTS1dUVmZmZOHfunNjnyJEjKCwsRMuWLSvg1X1c+DUHERFVOoWFhQgPD4evr684+wC8mkEoaabAxsYGdnZ24nN7e3sEBwfjq6++KtNNIx0cHNClSxeMGDECK1euxIsXLzB27Fj4+PjwTI4yYJggIqJK5/Dhw0hOThbvIq2o69evIysrS3xelptGRkZGYuzYsejUqRM0NDTg7e2NpUuXKv1aPgW80Vc58UZfHz/e6IuIPnW80RcRERG9F/yag4joE8EZ1Y+fumZUOTNBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSIiIlIKwwQREREphWGCiIiIlMIwQUREREpRa5iwtbWFRCIp9vD39wcAPH/+HP7+/jA1NYWBgQG8vb2L3Y+eiNTnn3/+waBBg2Bqago9PT04OTnh7Nmz4vKS/n9LJBL89NNPpY5ZUFCAadOmwc7ODnp6eqhTpw5++OEHvH4boR07dqBz584wNTWFRCIRb0NNROqh1jARHx+P1NRU8XHo0CEAQJ8+fQAAgYGB2LNnD7Zt24aYmBjcu3cPvXr1UmfJRPT/Hj9+jDZt2kBbWxv79+/HlStXsGDBAlSrVk3s8/r/79TUVKxduxYSiQTe3t6ljhsaGooVK1Zg+fLluHr1KkJDQzFv3jwsW7ZM7JOTk4O2bdsiNDS0Ql8jEZWNWu/NYWZmJvc8JCQEderUQfv27ZGVlYU1a9Zg06ZN6NixIwAgPDwcDg4OiI2NRatWrdRRMhH9v9DQUMhkMoSHh4ttdnZ2cn0sLS3lnv/666/o0KEDateuXeq4p06dgpeXF7p1e3WPAVtbW2zevBlnzpwR+wwePBgAkJSUpOzLICIVqDTHTOTn52Pjxo0YPnw4JBIJzp07hxcvXsDNzU3sY29vDxsbG5w+fbrUcfLy8pCdnS33ICLV2717N1xcXNCnTx+Ym5vD2dkZq1evLrV/eno69u3bBz8/v7eO27p1a0RHR+PGjRsAgEuXLuHEiRPw8PBQaf1EpDqVJkzs2rULmZmZGDp0KAAgLS0NVapUgbGxsVw/CwsLpKWllTpOcHAwpFKp+JDJZBVYNdGn69atW1ixYgXq1auHgwcPYvTo0Rg/fjzWrVtXYv9169bB0NDwnV9VTp06FT4+PrC3t4e2tjacnZ0REBCAgQMHVsTLICIVqDS3IF+zZg08PDxgbW2t1DhBQUGYMGGC+Dw7O5uBgqgCFBYWwsXFBXPnzgUAODs74/Lly1i5ciV8fX2L9V+7di0GDhwIXV3dt467detWREZGYtOmTXB0dMTFixcREBAAa2vrEsclIvWrFGHizp07OHz4MHbs2CG2WVpaIj8/H5mZmXKzE+np6cW+h32djo4OdHR0KrJcIgJgZWWFhg0byrU5ODjgl19+Kdb3jz/+wPXr17Fly5Z3jjt58mRxdgIAnJyccOfOHQQHBzNMEFVSleJrjvDwcJibm4sHXAFA8+bNoa2tjejoaLHt+vXrSE5OhqurqzrKJKLXtGnTBtevX5dru3HjBmrVqlWs75o1a9C8eXM0adLknePm5uZCQ0P+o0lTUxOFhYXKFUxEFUbtMxOFhYUIDw+Hr68vtLT+V45UKoWfnx8mTJgAExMTGBkZYdy4cXB1deWZHESVQGBgIFq3bo25c+eib9++OHPmDFatWoVVq1bJ9cvOzsa2bduwYMGCEsfp1KkTvvrqK4wdOxYA4OnpiTlz5sDGxgaOjo64cOECFi5ciOHDh4vrPHr0CMnJybh37x4AiKHG0tLyrTOXRFQx1B4mDh8+jOTkZLkPiiKLFi2ChoYGvL29kZeXB3d3d/z8889qqJKI3tSiRQvs3LkTQUFBmD17Nuzs7LB48eJiB0pGRUVBEAT079+/xHESExORkZEhPl+2bBmmTZuGMWPG4P79+7C2tsaoUaMwffp0sc/u3bsxbNgw8XnRVyIzZszAzJkzVfgqiagsJMLrl5X7CGVnZ0MqlSIrKwtGRkYqG9d26j6VjUWVU1JIt3d3IvqA8HPr46fqz62y/gytFMdMEBER0YdL7V9zEJE8/vb48eOsF31sODNBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSIiIlIKwwQREREphWGCiIiIlMIwQUREREphmCAiIiKlMEwQERGRUhgmiIiISCkME0RERKQUhgkiIiJSCsMEERERKYVhgoiIiJTCMEFERERKYZggIiIipTBMEBERkVIYJoiIiEgpDBNERESkFIYJIiIiUoraw8Q///yDQYMGwdTUFHp6enBycsLZs2fF5YIgYPr06bCysoKenh7c3Nxw8+ZNNVZMREREr1NrmHj8+DHatGkDbW1t7N+/H1euXMGCBQtQrVo1sc+8efOwdOlSrFy5EnFxcdDX14e7uzueP3+uxsqJiIioiJY6Nx4aGgqZTIbw8HCxzc7OTvy7IAhYvHgxvv/+e3h5eQEA1q9fDwsLC+zatQs+Pj7vvWYiIiKSp9aZid27d8PFxQV9+vSBubk5nJ2dsXr1anH57du3kZaWBjc3N7FNKpWiZcuWOH36dIlj5uXlITs7W+5BREREFUetYeLWrVtYsWIF6tWrh4MHD2L06NEYP3481q1bBwBIS0sDAFhYWMitZ2FhIS57U3BwMKRSqfiQyWQV+yKIiIg+cWoNE4WFhWjWrBnmzp0LZ2dnjBw5EiNGjMDKlSvLPWZQUBCysrLER0pKigorJiIiojepNUxYWVmhYcOGcm0ODg5ITk4GAFhaWgIA0tPT5fqkp6eLy96ko6MDIyMjuQcRERFVHIXDRE5Ojso23qZNG1y/fl2u7caNG6hVqxaAVwdjWlpaIjo6WlyenZ2NuLg4uLq6qqwOIiIiKj+Fw4SFhQWGDx+OEydOKL3xwMBAxMbGYu7cuUhISMCmTZuwatUq+Pv7AwAkEgkCAgLw448/Yvfu3fjrr78wZMgQWFtbo2fPnkpvn4iIiJSncJjYuHEjHj16hI4dO6J+/foICQnBvXv3yrXxFi1aYOfOndi8eTMaNWqEH374AYsXL8bAgQPFPlOmTMG4ceMwcuRItGjRAk+fPsWBAwegq6tbrm0SERGRakkEQRDKs+KDBw+wYcMGRERE4OrVq3B3d8fw4cPRo0cPaGmp9fIVcrKzsyGVSpGVlaXS4ydsp+5T2VhUOSWFdFPLdrlvffy4b1FFUfW+VdafoeU+ANPMzAwTJkzAn3/+iYULF+Lw4cPo3bs3rK2tMX36dOTm5pZ3aCIiIvqAlHsKIT09HevWrUNERATu3LmD3r17w8/PD3fv3kVoaChiY2Px+++/q7JWIiIiqoQUDhM7duxAeHg4Dh48iIYNG2LMmDEYNGgQjI2NxT6tW7eGg4ODKuskIiKiSkrhMDFs2DD4+Pjg5MmTaNGiRYl9rK2t8e9//1vp4oiIiKjyUzhMpKamomrVqm/to6enhxkzZpS7KCIiIvpwKHwA5rFjx3Dw4MFi7QcPHsT+/ftVUhQRERF9OBQOE1OnTkVBQUGxdkEQMHXqVJUURURERB8OhcPEzZs3i91PAwDs7e2RkJCgkqKIiIjow6FwmJBKpbh161ax9oSEBOjr66ukKCIiIvpwKBwmvLy8EBAQgMTERLEtISEBEydORI8ePVRaHBEREVV+CoeJefPmQV9fH/b29rCzs4OdnR0cHBxgamqK+fPnV0SNREREVIkpfGqoVCrFqVOncOjQIVy6dAl6enpo3Lgx2rVrVxH1ERERUSVXrstpSyQSdO7cGZ07d1Z1PURERPSBKVeYyMnJQUxMDJKTk5Gfny+3bPz48SopjIiIiD4MCoeJCxcuoGvXrsjNzUVOTg5MTEyQkZGBqlWrwtzcnGGCiIjoE6PwAZiBgYHw9PTE48ePoaenh9jYWNy5cwfNmzfnAZhERESfIIXDxMWLFzFx4kRoaGhAU1MTeXl5kMlkmDdvHr777ruKqJGIiIgqMYXDhLa2NjQ0Xq1mbm6O5ORkAK/O8khJSVFtdURERFTpKXzMhLOzM+Lj41GvXj20b98e06dPR0ZGBjZs2IBGjRpVRI1ERERUiSk8MzF37lxYWVkBAObMmYNq1aph9OjRePDgAVatWqXyAomIiKhyU2hmQhAEmJubizMQ5ubmOHDgQIUURkRERB8GhWYmBEFA3bp1eWwEERERiRQKExoaGqhXrx4ePnxYUfUQERHRB0bhYyZCQkIwefJkXL58uSLqISIiog+MwmFiyJAhOHPmDJo0aQI9PT2YmJjIPRQxc+ZMSCQSuYe9vb24/Pnz5/D394epqSkMDAzg7e2N9PR0RUsmIiKiCqTwqaGLFy9WaQGOjo44fPiw+FxL638lBQYGYt++fdi2bRukUinGjh2LXr164eTJkyqtgYiIiMpP4TDh6+ur2gK0tGBpaVmsPSsrC2vWrMGmTZvQsWNHAEB4eDgcHBwQGxuLVq1aqbQOIiIiKh+Fw0TRFS9LY2Njo9B4N2/ehLW1NXR1deHq6org4GDY2Njg3LlzePHiBdzc3MS+9vb2sLGxwenTp0sNE3l5ecjLyxOfZ2dnK1QPERERKUbhMGFrawuJRFLq8oKCgjKP1bJlS0RERKBBgwZITU3FrFmz8Pnnn+Py5ctIS0tDlSpVYGxsLLeOhYUF0tLSSh0zODgYs2bNKnMNREREpJxy3YL8dS9evMCFCxewcOFCzJkzR6GxPDw8xL83btwYLVu2RK1atbB161bo6ekpWhoAICgoCBMmTBCfZ2dnQyaTlWssIiIiejeFw0STJk2Ktbm4uMDa2ho//fQTevXqVe5ijI2NUb9+fSQkJODLL79Efn4+MjMz5WYn0tPTSzzGooiOjg50dHTKXQMREREpRuFTQ0vToEEDxMfHKzXG06dPkZiYCCsrKzRv3hza2tqIjo4Wl1+/fh3JyclwdXVVtlwiIiJSEYVnJt48oFEQBKSmpmLmzJmoV6+eQmNNmjQJnp6eqFWrFu7du4cZM2ZAU1MT/fv3h1QqhZ+fHyZMmAATExMYGRlh3LhxcHV15ZkcRERElYjCYcLY2LjYAZiCIEAmkyEqKkqhse7evYv+/fvj4cOHMDMzQ9u2bREbGwszMzMAwKJFi6ChoQFvb2/k5eXB3d0dP//8s6IlExERUQVSOEwcOXJELkxoaGjAzMwMdevWlbvgVFm8K3zo6uoiLCwMYWFhipZJRERE74nCYeKLL76ogDKIiIjoQ6XwAZjBwcFYu3Ztsfa1a9ciNDRUJUURERHRh0PhMPGf//xH7mZcRRwdHbFy5UqVFEVEREQfDoXDRFpaGqysrIq1m5mZITU1VSVFERER0YdD4TAhk8lKvGvnyZMnYW1trZKiiIiI6MOh8AGYI0aMQEBAAF68eCHezTM6OhpTpkzBxIkTVV4gERERVW4Kh4nJkyfj4cOHGDNmDPLz8wG8OoXz22+/xdSpU1VeIBEREVVuCocJiUSC0NBQTJs2DVevXoWenh7q1avH+2EQERF9ohQOE1lZWSgoKICJiQlatGghtj969AhaWlowMjJSaYFERERUuSl8AKaPj0+JV67cunUrfHx8VFIUERERfTgUDhNxcXHo0KFDsfYvvvgCcXFxKimKiIiIPhwKh4m8vDy8fPmyWPuLFy/w7NkzlRRFREREHw6Fw8Rnn32GVatWFWtfuXIlmjdvrpKiiIiI6MOh8AGYP/74I9zc3HDp0iV06tQJwKvrTMTHx+P3339XeYFERERUuSk8M9GmTRucPn0aMpkMW7duxZ49e1C3bl38+eef+PzzzyuiRiIiIqrEFJ6ZAICmTZsiMjJSrq2wsBB79+5F9+7dVVIYERERfRjKFSZel5CQgLVr1yIiIgIPHjzAixcvVFEXERERfSAU/poDAJ49e4b169ejXbt2aNCgAU6dOoXp06fj7t27qq6PiIiIKjmFZibi4+Px3//+F1FRUahTpw4GDhyIU6dO4eeff0bDhg0rqkYiIiKqxMocJho3bozs7GwMGDAAp06dgqOjIwDw5l5ERESfuDJ/zXH9+nW0a9cOHTp04CwEERERicocJm7duoUGDRpg9OjRqFmzJiZNmoQLFy5AIpFUZH1ERERUyZU5TNSoUQP//ve/kZCQgA0bNiAtLQ1t2rTBy5cvERERgRs3blRknURERFRJletsjo4dO2Ljxo1ITU3F8uXLceTIEdjb26Nx48aqro+IiIgquXKFiSJSqRRjxozB2bNncf78eXzxxRcqKouIiIg+FEqFidc1bdoUS5cuLff6ISEhkEgkCAgIENueP38Of39/mJqawsDAAN7e3khPT1dBtURERKQqKgsTyoiPj8d//vOfYl+TBAYGYs+ePdi2bRtiYmJw79499OrVS01VEhERUUnUHiaePn2KgQMHYvXq1ahWrZrYnpWVhTVr1mDhwoXo2LEjmjdvjvDwcJw6dQqxsbGljpeXl4fs7Gy5BxEREVUctYcJf39/dOvWDW5ubnLt586dw4sXL+Ta7e3tYWNjg9OnT5c6XnBwMKRSqfiQyWQVVjsRERGpOUxERUXh/PnzCA4OLrYsLS0NVapUgbGxsVy7hYUF0tLSSh0zKCgIWVlZ4iMlJUXVZRMREdFrynQ5bUUOrBw/fnyZ+qWkpOBf//oXDh06BF1d3TKP/y46OjrQ0dFR2XhERET0dmUKE4sWLSrTYBKJpMxh4ty5c7h//z6aNWsmthUUFOD48eNYvnw5Dh48iPz8fGRmZsrNTqSnp8PS0rJM2yAiIqKKV6Ywcfv2bZVvuFOnTvjrr7/k2oYNGwZ7e3t8++23kMlk0NbWRnR0NLy9vQG8uj9IcnIyXF1dVV4PERERlY9CtyB/XX5+Pm7fvo06depAS0vxYQwNDdGoUSO5Nn19fZiamortfn5+mDBhAkxMTGBkZIRx48bB1dUVrVq1Km/ZREREpGIKH4CZm5sLPz8/VK1aFY6OjkhOTgYAjBs3DiEhISotbtGiRejevTu8vb3Rrl07WFpaYseOHSrdBhERESlH4TARFBSES5cu4dixY3IHTrq5uWHLli1KFXPs2DEsXrxYfK6rq4uwsDA8evQIOTk52LFjB4+XICIiqmQU/n5i165d2LJlC1q1aiV3+3FHR0ckJiaqtDgiIiKq/BSemXjw4AHMzc2Ltefk5MiFCyIiIvo0KBwmXFxcsG/fPvF5UYD473//y7MsiIiIPkEKf80xd+5ceHh44MqVK3j58iWWLFmCK1eu4NSpU4iJiamIGomIiKgSU3hmom3btrh48SJevnwJJycn/P777zA3N8fp06fRvHnziqiRiIiIKrFyXWeiTp06WL16taprISIiog9QmcKEIrfxNjIyKncxRERE9OEpU5gwNjYu85kaBQUFShVEREREH5YyhYmjR4+Kf09KSsLUqVMxdOhQ8eyN06dPY926dSXeSpyIiIg+bmUKE+3btxf/Pnv2bCxcuBD9+/cX23r06AEnJyesWrUKvr6+qq+SiIiIKi2Fz+Y4ffo0XFxcirW7uLjgzJkzKimKiIiIPhwKhwmZTFbimRz//e9/IZPJVFIUERERfTgUPjV00aJF8Pb2xv79+9GyZUsAwJkzZ3Dz5k388ssvKi+QiIiIKjeFZya6du2KmzdvwtPTE48ePcKjR4/g6emJGzduoGvXrhVRIxEREVVi5bpoVc2aNTF37lxV10JEREQfoHKFiczMTKxZswZXr14F8Or248OHD4dUKlVpcURERFT5Kfw1x9mzZ1GnTh0sWrRI/Jpj4cKFqFOnDs6fP18RNRIREVElpvDMRGBgIHr06IHVq1dDS+vV6i9fvsTXX3+NgIAAHD9+XOVFEhERUeWlcJg4e/asXJAAAC0tLUyZMqXE608QERHRx03hrzmMjIyQnJxcrD0lJQWGhoYqKYqIiIg+HAqHiX79+sHPzw9btmxBSkoKUlJSEBUVha+//lruEttERET0aVD4a4758+dDIpFgyJAhePnyJQBAW1sbo0ePRkhIiMoLJCIiospN4TBRpUoVLFmyBMHBwUhMTAQA1KlTB1WrVlV5cURERFT5les6EwBQtWpVODk5qbIWIiIi+gCVOUwMHz68TP3Wrl1b5o2vWLECK1asQFJSEoBXF7+aPn06PDw8AADPnz/HxIkTERUVhby8PLi7u+Pnn3+GhYVFmbdBREREFavMYSIiIgK1atWCs7MzBEFQycZr1qyJkJAQ1KtXD4IgYN26dfDy8sKFCxfg6OiIwMBA7Nu3D9u2bYNUKsXYsWPRq1cvnDx5UiXbJyIiIuWVOUyMHj0amzdvxu3btzFs2DAMGjQIJiYmSm3c09NT7vmcOXOwYsUKxMbGombNmlizZg02bdqEjh07AgDCw8Ph4OCA2NhYtGrVSqltExERkWqU+dTQsLAwpKamYsqUKdizZw9kMhn69u2LgwcPqmSmoqCgAFFRUcjJyYGrqyvOnTuHFy9ewM3NTexjb28PGxsbnD59utRx8vLykJ2dLfcgIiKiiqPQdSZ0dHTQv39/HDp0CFeuXIGjoyPGjBkDW1tbPH36tFwF/PXXXzAwMICOjg6++eYb7Ny5Ew0bNkRaWhqqVKkCY2Njuf4WFhZIS0srdbzg4GBIpVLxIZPJylUXERERlY3CF60SV9TQgEQigSAIKCgoKHcBDRo0wMWLFxEXF4fRo0fD19cXV65cKfd4QUFByMrKEh8pKSnlHouIiIjeTaEwkZeXh82bN+PLL79E/fr18ddff2H58uVITk6GgYFBuQqoUqUK6tati+bNmyM4OBhNmjTBkiVLYGlpifz8fGRmZsr1T09Ph6WlZanj6ejowMjISO5BREREFafMB2COGTMGUVFRkMlkGD58ODZv3ozq1aurvKDCwkLk5eWhefPm0NbWRnR0NLy9vQEA169fR3JyMlxdXVW+XSIiIiqfMoeJlStXwsbGBrVr10ZMTAxiYmJK7Ldjx44ybzwoKAgeHh6wsbHBkydPsGnTJhw7dgwHDx6EVCqFn58fJkyYABMTExgZGWHcuHFwdXXlmRxERESVSJnDxJAhQyCRSFS68fv372PIkCFITU2FVCpF48aNcfDgQXz55ZcAgEWLFkFDQwPe3t5yF60iIiKiykOhi1ap2po1a966XFdXF2FhYQgLC1P5tomIiEg1yn02BxERERHAMEFERERKYpggIiIipTBMEBERkVIYJoiIiEgpDBNERESkFIYJIiIiUgrDBBERESmFYYKIiIiUwjBBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSIiIlIKwwQREREphWGCiIiIlMIwQUREREphmCAiIiKlMEwQERGRUhgmiIiISCkME0RERKQUhgkiIiJSCsMEERERKUWtYSI4OBgtWrSAoaEhzM3N0bNnT1y/fl2uz/Pnz+Hv7w9TU1MYGBjA29sb6enpaqqYiIiI3qTWMBETEwN/f3/Exsbi0KFDePHiBTp37oycnByxT2BgIPbs2YNt27YhJiYG9+7dQ69evdRYNREREb1OS50bP3DggNzziIgImJub49y5c2jXrh2ysrKwZs0abNq0CR07dgQAhIeHw8HBAbGxsWjVqpU6yiYiIqLXVKpjJrKysgAAJiYmAIBz587hxYsXcHNzE/vY29vDxsYGp0+fLnGMvLw8ZGdnyz2IiIio4lSaMFFYWIiAgAC0adMGjRo1AgCkpaWhSpUqMDY2lutrYWGBtLS0EscJDg6GVCoVHzKZrKJLJyIi+qRVmjDh7++Py5cvIyoqSqlxgoKCkJWVJT5SUlJUVCERERGVRK3HTBQZO3Ys9u7di+PHj6NmzZpiu6WlJfLz85GZmSk3O5Geng5LS8sSx9LR0YGOjk5Fl0xERET/T60zE4IgYOzYsdi5cyeOHDkCOzs7ueXNmzeHtrY2oqOjxbbr168jOTkZrq6u77tcIiIiKoFaZyb8/f2xadMm/PrrrzA0NBSPg5BKpdDT04NUKoWfnx8mTJgAExMTGBkZYdy4cXB1deWZHERERJWEWsPEihUrAABffPGFXHt4eDiGDh0KAFi0aBE0NDTg7e2NvLw8uLu74+eff37PlRIREVFp1BomBEF4Zx9dXV2EhYUhLCzsPVREREREiqo0Z3MQERHRh4lhgoiIiJTCMEFERERKYZggIiIipTBMEBERkVIYJoiIiEgpDBNERESkFIYJIiIiUgrDBBERESmFYYKIiIiUwjBBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSIiIlIKwwQREREphWGCiIiIlMIwQUREREphmCAiIiKlMEwQERGRUhgmiIiISCkME0RERKQUhgkiIiJSilrDxPHjx+Hp6Qlra2tIJBLs2rVLbrkgCJg+fTqsrKygp6cHNzc33Lx5Uz3FEhERUYnUGiZycnLQpEkThIWFlbh83rx5WLp0KVauXIm4uDjo6+vD3d0dz58/f8+VEhERUWm01LlxDw8PeHh4lLhMEAQsXrwY33//Pby8vAAA69evh4WFBXbt2gUfH5/3WSoRERGVotIeM3H79m2kpaXBzc1NbJNKpWjZsiVOnz5d6np5eXnIzs6WexAREVHFqbRhIi0tDQBgYWEh125hYSEuK0lwcDCkUqn4kMlkFVonERHRp67ShonyCgoKQlZWlvhISUlRd0lEREQftUobJiwtLQEA6enpcu3p6enispLo6OjAyMhI7kFEREQVp9KGCTs7O1haWiI6Olpsy87ORlxcHFxdXdVYGREREb1OrWdzPH36FAkJCeLz27dv4+LFizAxMYGNjQ0CAgLw448/ol69erCzs8O0adNgbW2Nnj17qq9oIiIikqPWMHH27Fl06NBBfD5hwgQAgK+vLyIiIjBlyhTk5ORg5MiRyMzMRNu2bXHgwAHo6uqqq2QiIiJ6g1rDxBdffAFBEEpdLpFIMHv2bMyePfs9VkVERESKqLTHTBAREdGHgWGCiIiIlMIwQUREREphmCAiIiKlMEwQERGRUhgmiIiISCkME0RERKQUhgkiIiJSCsMEERERKYVhgoiIiJTCMEFERERKYZggIiIipTBMEBERkVIYJoiIiEgpDBNERESkFIYJIiIiUgrDBBERESmFYYKIiIiUwjBBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSIiIlLKBxEmwsLCYGtrC11dXbRs2RJnzpxRd0lERET0/yp9mNiyZQsmTJiAGTNm4Pz582jSpAnc3d1x//59dZdGRERE+ADCxMKFCzFixAgMGzYMDRs2xMqVK1G1alWsXbtW3aURERERAC11F/A2+fn5OHfuHIKCgsQ2DQ0NuLm54fTp0yWuk5eXh7y8PPF5VlYWACA7O1ultRXm5ap0PKp8VL3PlBX3rY8f9y2qKKret4rGEwThrf0qdZjIyMhAQUEBLCws5NotLCxw7dq1EtcJDg7GrFmzirXLZLIKqZE+XtLF6q6APlbct6iiVNS+9eTJE0il0lKXV+owUR5BQUGYMGGC+LywsBCPHj2CqakpJBKJGiv7cGVnZ0MmkyElJQVGRkbqLoc+Ity3qKJw31INQRDw5MkTWFtbv7VfpQ4T1atXh6amJtLT0+Xa09PTYWlpWeI6Ojo60NHRkWszNjauqBI/KUZGRvxPSRWC+xZVFO5bynvbjESRSn0AZpUqVdC8eXNER0eLbYWFhYiOjoarq6saKyMiIqIilXpmAgAmTJgAX19fuLi44LPPPsPixYuRk5ODYcOGqbs0IiIiwgcQJvr164cHDx5g+vTpSEtLQ9OmTXHgwIFiB2VSxdHR0cGMGTOKfX1EpCzuW1RRuG+9XxLhXed7EBEREb1FpT5mgoiIiCo/hgkiIiJSCsMEERERKYVh4hOWlJQEiUSCixcvqrsUokrpiy++QEBAgLrLoI+Ara0tFi9erO4yKgzDRAVLS0vDuHHjULt2bejo6EAmk8HT01Pu2hkfElV9uB47dgwSiQQSiQQaGhqQSqVwdnbGlClTkJqaqvB4EokEu3btUrquymTo0KGQSCT45ptvii3z9/eHRCLB0KFD339hb4iIiKg0F4Yrby1F+2NmZqZc+44dO/DDDz+oprhKbOjQoejZs6dc2/bt26Grq4sFCxaIfSQSCUJCQuT67dq1S+7qwkXvpaOjIwoKCuT6GhsbIyIiotQ6Zs6ciaZNmyr1WlSlvLWUtg/Gx8dj5MiRyhdWSTFMVKCkpCQ0b94cR44cwU8//YS//voLBw4cQIcOHeDv76/u8iqF69ev4969e4iPj8e3336Lw4cPo1GjRvjrr7/UXVqlIJPJEBUVhWfPnoltz58/x6ZNm2BjY6PGyj4NJiYmMDQ0VHcZ791///tfDBw4ECtWrMDEiRPFdl1dXYSGhuLx48fvHOPWrVtYv359RZb5QTEzM0PVqlXVXUaFYZioQGPGjIFEIsGZM2fg7e2N+vXrw9HRERMmTEBsbKzYLzk5GV5eXjAwMICRkRH69u0rdwnxooS8du1a2NjYwMDAAGPGjEFBQQHmzZsHS0tLmJubY86cOXLbl0gkWLFiBTw8PKCnp4fatWtj+/btb6358uXL8PDwgIGBASwsLDB48GBkZGQAePWbSUxMDJYsWSLOKiQlJb1zvbcxNzeHpaUl6tevDx8fH5w8eRJmZmYYPXq02Cc+Ph5ffvklqlevDqlUivbt2+P8+fPicltbWwDAV199BYlEIj5PTEyEl5cXLCwsYGBggBYtWuDw4cPvrKkyadasGWQyGXbs2CG27dixAzY2NnB2dpbrW1hYiODgYNjZ2UFPTw9NmjSR+/cuKCiAn5+fuLxBgwZYsmSJ3BhFv6HOnz8fVlZWMDU1hb+/P168eFHmmitqfy1p9uDixYvifnjs2DEMGzYMWVlZ4v45c+ZMAMCGDRvg4uICQ0NDWFpaYsCAAbh//z6AV6G/Q4cOAIBq1arJzfi8ORP3+PFjDBkyBNWqVUPVqlXh4eGBmzdvisuLfis9ePAgHBwcYGBggC5dupRrtk1d5s2bh3HjxiEqKqrYxQHd3NxgaWmJ4ODgd44zbtw4zJgxQ+4uzooq2h/nzp0LCwsLGBsbY/bs2Xj58iUmT54MExMT1KxZE+Hh4eI6RV/fRkVFoXXr1tDV1UWjRo0QExMj9ilp9uD1GZaIiAjMmjULly5dEvelohmVhQsXwsnJCfr6+pDJZBgzZgyePn0KAG/dB9/8mqOsn/sbNmyAra0tpFIpfHx88OTJk3K/nxWJYaKCPHr0CAcOHIC/vz/09fWLLS/akQsLC+Hl5YVHjx4hJiYGhw4dwq1bt9CvXz+5/omJidi/fz8OHDiAzZs3Y82aNejWrRvu3r2LmJgYhIaG4vvvv0dcXJzcetOmTYO3tzcuXbqEgQMHwsfHB1evXi2x5szMTHTs2BHOzs44e/YsDhw4gPT0dPTt2xcAsGTJEri6umLEiBFITU1FamoqZDLZO9dThJ6eHr755hucPHlS/LB/8uQJfH19ceLECcTGxqJevXro2rWr+J8qPj4eABAeHo7U1FTx+dOnT9G1a1dER0fjwoUL6NKlCzw9PZGcnKxwXeo0fPhwuQ/LtWvXlngF2ODgYKxfvx4rV67E33//jcDAQAwaNEj8EC0sLETNmjWxbds2XLlyBdOnT8d3332HrVu3yo1z9OhRJCYm4ujRo1i3bh0iIiLeOjVdkvexv76pdevWWLx4MYyMjMT9c9KkSQCAFy9e4IcffsClS5ewa9cuJCUliYFBJpPhl19+AfBqpiw1NbVYyCoydOhQnD17Frt378bp06chCAK6du0qF7Zyc3Mxf/58bNiwAcePH0dycrJYR2X37bff4ocffsDevXvx1VdfFVuuqamJuXPnYtmyZbh79+5bxwoICMDLly+xbNkypWo6cuQI7t27h+PHj2PhwoWYMWMGunfvjmrVqiEuLg7ffPMNRo0aVayeyZMnY+LEibhw4QJcXV3h6emJhw8flmmb/fr1w8SJE+Ho6CjuS0WfyRoaGli6dCn+/vtvrFu3DkeOHMGUKVMAvH0ffJ0in/u7du3C3r17sXfvXsTExBT7mqnSEKhCxMXFCQCEHTt2vLXf77//LmhqagrJycli299//y0AEM6cOSMIgiDMmDFDqFq1qpCdnS32cXd3F2xtbYWCggKxrUGDBkJwcLD4HIDwzTffyG2vZcuWwujRowVBEITbt28LAIQLFy4IgiAIP/zwg9C5c2e5/ikpKQIA4fr164IgCEL79u2Ff/3rX3J9yrLem44ePSoAEB4/flxs2f79+wUAQlxcXInrFhQUCIaGhsKePXvkXuvOnTtL7P86R0dHYdmyZe/sVxn4+voKXl5ewv379wUdHR0hKSlJSEpKEnR1dYUHDx4IXl5egq+vryAIgvD8+XOhatWqwqlTp+TG8PPzE/r371/qNvz9/QVvb2+5bdaqVUt4+fKl2NanTx+hX79+pY4RHh4uSKVS8XlF7a8l7TMXLlwQAAi3b98usZbSxMfHCwCEJ0+elDq2IMjv7zdu3BAACCdPnhSXZ2RkCHp6esLWrVvF7QMQEhISxD5hYWGChYXFO2tSJ19fX6FKlSoCACE6OrrUPl5eXoIgCEKrVq2E4cOHC4IgCDt37hRe/1Hy+nu5cuVKwcTERMjMzBQEQRCkUqkQHh5eah0zZswQmjRpIrfNWrVqFdtvPv/8c/H5y5cvBX19fWHz5s2CIPzvcy0kJETs8+LFC6FmzZpCaGioIAgl7ydvvo43aynNtm3bBFNTU/F5aftgrVq1hEWLFgmCUP7P/cmTJwstW7Z8Z03qwJmJCiKU8cKiV69ehUwmg0wmE9saNmwIY2Njud/IbG1t5b67tbCwQMOGDaGhoSHXVvTbfJE3b4jm6upa6m96ly5dwtGjR2FgYCA+7O3tAbxKyKUp73qlKXrviqYc09PTMWLECNSrVw9SqRRGRkZ4+vTpO2cYnj59ikmTJsHBwQHGxsYwMDDA1atXP7iZCTMzM3Tr1g0REREIDw9Ht27dUL16dbk+CQkJyM3NxZdffin377B+/Xq5f4OwsDA0b94cZmZmMDAwwKpVq4q9H46OjtDU1BSfW1lZFduv3uV97K+KOHfuHDw9PWFjYwNDQ0O0b98eABTaF65evQotLS20bNlSbDM1NUWDBg3kaqxatSrq1KkjPi/P+6cOjRs3hq2tLWbMmCFO25cmNDQU69ate+e/jZ+fH0xNTREaGlruuhwdHYvtN05OTuJzTU1NmJqavnVf0tLSgouLi0r2pcOHD6NTp06oUaMGDA0NMXjwYDx8+BC5ubllHqO8n/uVeV+q9Pfm+FDVq1cPEokE165dU8l42tracs8lEkmJbYWFheXextOnT+Hp6Vnif3wrKyuVr1eaov9MRcc++Pr64uHDh1iyZAlq1aoFHR0duLq6Ij8//63jTJo0CYcOHcL8+fNRt25d6OnpoXfv3u9crzIaPnw4xo4dC+BVIHhT0Yf/vn37UKNGDbllRfcmiIqKwqRJk7BgwQK4urrC0NAQP/30U7GvGlSxX1XE/lr0A+X1oF6WYzlycnLg7u4Od3d3REZGwszMDMnJyXB3d6+QfaGk11nWXy7UqUaNGti+fTs6dOiALl26YP/+/aUefNquXTu4u7sjKCjorWcUaWlpYc6cORg6dKi4/yqqovalN/9NyrIvJSUloXv37hg9ejTmzJkDExMTnDhxAn5+fsjPz1f5AZaq/oyvSJyZqCAmJiZwd3dHWFgYcnJyii0vOojMwcEBKSkpSElJEZdduXIFmZmZaNiwodJ1vH6gZ9FzBweHEvs2a9YMf//9N2xtbVG3bl25R9FxH1WqVCl2uldZ1iurZ8+eYdWqVWjXrh3MzMwAACdPnsT48ePRtWtXODo6QkdHp9jBndra2sXqOnnyJIYOHYqvvvoKTk5OsLS0FA8Y/dB06dIF+fn5ePHiBdzd3Ystb9iwIXR0dJCcnFzs36Dot5+TJ0+idevWGDNmDJydnVG3bt1yzRxVpLftr0X7w+sHM755jZSS9s9r167h4cOHCAkJweeffw57e/tiv91VqVIFAIqt+zoHBwe8fPlSLnw9fPgQ169fV8n/1cqgVq1aiImJQVpaGrp06fLWg/1CQkKwZ88enD59+q1j9unTB46Ojpg1a5aqy32r1/elly9f4ty5c3L70pMnT+Q+m8uyL507dw6FhYVYsGABWrVqhfr16+PevXvvXO9NFf25rw4MExUoLCwMBQUF+Oyzz/DLL7/g5s2buHr1KpYuXSpOwbm5ucHJyQkDBw7E+fPncebMGQwZMgTt27eHi4uL0jVs27YNa9euxY0bNzBjxgycOXOm1N8Q/P398ejRI/Tv3x/x8fFITEzEwYMHMWzYMPE/h62tLeLi4pCUlISMjAwUFhaWab3S3L9/H2lpabh58yaioqLQpk0bZGRkYMWKFWKfevXqYcOGDbh69Sri4uIwcOBA6OnpyY1ja2uL6OhopKWliaet1atXDzt27MDFixdx6dIlDBgwoNKm+nfR1NTE1atXceXKFbmvIIoYGhpi0qRJCAwMxLp165CYmIjz589j2bJlWLduHYBX78fZs2dx8OBB3LhxA9OmTRMPVq0s3ra/FgWjmTNn4ubNm9i3b594DYQitra2ePr0KaKjo5GRkYHc3FzY2NigSpUqWLZsGW7duoXdu3cXu3ZErVq1IJFIsHfvXjx48KDEaf569erBy8sLI0aMwIkTJ3Dp0iUMGjQINWrUgJeXV8W9Ke+ZTCbDsWPHcP/+fbi7uyM7O7vEfkWfW0uXLn3nmCEhIVi7dm2Jv1hVlLCwMOzcuRPXrl2Dv78/Hj9+jOHDhwMAWrZsiapVq+K7775DYmIiNm3aVOwgY1tbW9y+fRsXL15ERkYG8vLyULduXbx48ULclzZs2ICVK1cWW+/NffBNFf25rw4MExWodu3aOH/+PDp06ICJEyeiUaNG+PLLLxEdHS3+sJRIJPj1119RrVo1tGvXDm5ubqhduza2bNmikhpmzZqFqKgoNG7cGOvXr8fmzZtLTb7W1tY4efIkCgoK0LlzZzg5OSEgIADGxsbiFPOkSZOgqamJhg0bitPFZVmvNA0aNIC1tTWaN2+OkJAQuLm54fLly3I1rlmzBo8fP0azZs0wePBgjB8/Hubm5nLjLFiwAIcOHYJMJhNPmVy4cCGqVauG1q1bw9PTE+7u7mjWrJkyb6daGRkZwcjIqNTlP/zwA6ZNm4bg4GA4ODigS5cu2LdvH+zs7AAAo0aNQq9evdCvXz+0bNkSDx8+xJgxY95X+WXytv1VW1sbmzdvxrVr19C4cWOEhobixx9/lFu/devW+Oabb9CvXz+YmZlh3rx5MDMzQ0REBLZt24aGDRsiJCQE8+fPl1uvRo0amDVrFqZOnQoLC4tSA3d4eDiaN2+O7t27w9XVFYIg4Lfffis2Hf2hq1mzJo4dO4aMjIy3BorZs2eXKaB37NgRHTt2xMuXL1VdaqlCQkIQEhKCJk2a4MSJE9i9e7d4rJGJiQk2btyI3377DU5OTti8ebN4CmcRb29vdOnSBR06dICZmRk2b96MJk2aYOHChQgNDUWjRo0QGRlZ7DTZkvbBN1X057468BbkHzGJRIKdO3cWu7IdUWXE/ZVUISkpCXZ2drhw4UKluZrmp4AzE0RERKQUhgkiIiJSCr/mICIiIqVwZoKIiIiUwjBBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSJSikQieevjzcsUE9HHh7cgJyKlvH4Xzy1btmD69Om4fv262GZgYKCOsojoPeLMBBEpxdLSUnxIpVJIJBJYWlrC0NAQ9evXx4EDB+T679q1C/r6+njy5AmSkpIgkUgQFRWF1q1bQ1dXF40aNUJMTIzcOpcvX4aHhwcMDAxgYWGBwYMHF7sNPRGpD8MEEVUIfX19+Pj4IDw8XK49PDwcvXv3hqGhodg2efJkTJw4ERcuXICrqys8PT3x8OFDAEBmZiY6duwIZ2dnnD17FgcOHEB6ejr69u37Xl8PEZWOYYKIKszXX3+NgwcPil+F3L9/H7/99huGDx8u12/s2LHw9vaGg4MDVqxYAalUijVr1gAAli9fDmdnZ8ydOxf29vZwdnbG2rVrcfToUdy4ceO9vyYiKo5hgogqzGeffQZHR0esW7cOALBx40bUqlUL7dq1k+vn6uoq/l1LSwsuLi64evUqAODSpUs4evQoDAwMxIe9vT0AIDEx8T29EiJ6Gx6ASUQV6uuvv0ZYWBimTp2K8PBwDBs2DBKJpMzrP336FJ6enggNDS22zMrKSpWlElE5cWaCiCrUoEGDcOfOHSxduhRXrlyBr69vsT6xsbHi31++fIlz587BwcEBANCsWTP8/fffsLW1Rd26deUe+vr67+11EFHpGCaIqEJVq1YNvXr1wuTJk9G5c2fUrFmzWJ+wsDDs3LkT165dg7+/Px4/fiweV+Hv749Hjx6hf//+iI+PR2JiIg4ePIhhw4ahoKDgfb8cIioBwwQRVTg/Pz/k5+cXO/CySEhICEJCQtCkSROcOHECu3fvRvXq1QEA1tbWOHnyJAoKCtC5c2c4OTkhICAAxsbG0NDgRxhRZSARBEFQdxFE9HHbsGEDAgMDce/ePVSpUkVsT0pKgp2dHS5cuICmTZuqr0AiUgoPwCSiCpObm4vU1FSEhIRg1KhRckGCiD4enCMkogozb9482Nvbw9LSEkFBQeouh4gqCL/mICIiIqVwZoKIiIiUwjBBRERESmGYICIiIqUwTBAREZFSGCaIiIhIKQwTREREpBSGCSIiIlIKwwQREREp5f8AOSnmY2E9GPIAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 600x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(6,4))\n",
    "bars = plt.bar(g.Type, g.Accuracy)\n",
    "\n",
    "# Add values on top of each bar\n",
    "for bar in bars:\n",
    "    height = bar.get_height()\n",
    "    plt.text(\n",
    "        bar.get_x() + bar.get_width() / 2, height,\n",
    "        f'{height:.2f}', ha='center', va='bottom'\n",
    "    )\n",
    "\n",
    "# Additional plot settings\n",
    "plt.xlabel('Type')\n",
    "plt.ylabel('Model Accuracy')\n",
    "plt.title('Model Accuracy by Type')\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "id": "f1c8aeca-ce8a-46d8-a348-9d4990b6050e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 3 artists>"
      ]
     },
     "execution_count": 346,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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2mJjY9W6dWtlZ2e72vbu3auCggLFx8dffqUAAKBZ8Hjlo7q6WllZWRo5cqRatfr/p9vtdo0ZM0apqakKCQlRUFCQxo8fr/j4eN7pAgAAXDwOH5988okKCgo0evToWsfmzp2rFi1aKDk5WRUVFUpMTNQbb7zRIIUCAIDmwePwcdddd8myrPMe8/PzU2ZmpjIzMy+7MAAA0Dzx3S4AAMAowgcAADCqXm+1BVB/US982NQloIkdzBh88U5AM8bKBwAAMIrwAQAAjCJ8AAAAowgfAADAKMIHAAAwivABAACMInwAAACjCB8AAMAowgcAADCK8AEAAIwifAAAAKMIHwAAwCjCBwAAMIrwAQAAjCJ8AAAAowgfAADAKMIHAAAwivABAACMInwAAACjCB8AAMAowgcAADCK8AEAAIwifAAAAKMIHwAAwCjCBwAAMIrwAQAAjCJ8AAAAowgfAADAKI/Dx//93//poYceUmhoqPz9/dWjRw9t377dddyyLE2ZMkUdOnSQv7+/EhIStG/fvgYtGgAAeC+PwsexY8d08803q3Xr1vroo4/0zTff6LXXXlO7du1cfWbPnq358+dr0aJFysvLU9u2bZWYmKjTp083ePEAAMD7tPKk86xZs+R0OpWVleVqi46Odv3bsizNmzdPL774opKSkiRJy5Ytk8Ph0Nq1azV8+PAGKhsAAHgrj1Y+3n//fd144426//771b59e/Xu3Vt//etfXccPHDig4uJiJSQkuNrsdrvi4uKUm5t73jErKipUXl7utgEAgObLo/Dxww8/aOHChercubM2bNigJ598Uk8//bSWLl0qSSouLpYkORwOt/McDofr2LnS09Nlt9tdm9PprM/9AAAAXsKj8FFdXa0+ffrolVdeUe/evfX444/rscce06JFi+pdQFpamsrKylxbYWFhvccCAABXPo/CR4cOHdS1a1e3tpiYGBUUFEiSwsPDJUklJSVufUpKSlzHzuXr66ugoCC3DQAANF8ehY+bb75Ze/fudWv77rvv1KlTJ0m/XHwaHh6u7Oxs1/Hy8nLl5eUpPj6+AcoFAADezqN3u0ycOFH9+vXTK6+8ogceeEBbt27Vm2++qTfffFOSZLPZNGHCBL388svq3LmzoqOjNXnyZEVEROjee+9tjPoBAICX8Sh83HTTTVqzZo3S0tI0ffp0RUdHa968eRox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dbxmolZXVyspKUk///yzcnJy9PHHH+uHH37QsGHD3Prv379fH330kdavX68VK1Zo8eLFGjx4sH788Ufl5ORo1qxZevHFF5WXl+d23uTJk5WcnKzdu3drxIgRGj58uPbs2XPemktLSzVgwAD17t1b27dv1/r161VSUqIHHnhAkvT6668rPj5ejz32mA4dOqRDhw7J6XRe9DxP+Pv7a+zYsdq8ebPrj/7x48c1cuRIbdq0SVu2bFHnzp119913u35ptm3bJknKysrSoUOHXPsnTpzQ3XffrezsbO3cuVMDBw7UkCFDVFBQ4HFd3mD06NFufzTfeuut8346cHp6upYtW6ZFixbp66+/1sSJE/XQQw+5/phWV1erY8eOWrVqlb755htNmTJFf/7zn/Xuu++6jfPZZ59p//79+uyzz7R06VItWbLkgkvg52NiXp+rX79+mjdvnoKCglzzeNKkSZKkyspKzZgxQ7t379batWt18OBBV8BwOp36xz/+IemXFbtDhw7VCmU1Ro0ape3bt+v9999Xbm6uLMvS3Xff7RbOTp06pVdffVVvv/22Pv/8cxUUFLjqaC6ef/55zZgxQx988IHuu+++WsdbtmypV155RQsWLNCPP/54wbEmTJigs2fPasGCBZdV06effqqioiJ9/vnnmjNnjqZOnap77rlH7dq1U15ensaOHasnnniiVj3PPvusnnnmGe3cuVPx8fEaMmSIjh49ekm3OWzYMD3zzDPq1q2ba87V/I1v0aKF5s+fr6+//lpLly7Vp59+queee07Shefqr3nyOLJ27Vp98MEH+uCDD5STk1PrZa8rnoULysvLsyRZq1evvmC///mf/7FatmxpFRQUuNq+/vprS5K1detWy7Isa+rUqVabNm2s8vJyV5/ExEQrKirKqqqqcrXdcMMNVnp6umtfkjV27Fi324uLi7OefPJJy7Is68CBA5Yka+fOnZZlWdaMGTOsu+66y61/YWGhJcnau3evZVmWdfvtt1t/+tOf3Ppcynnn+uyzzyxJ1rFjx2od++ijjyxJVl5e3nnPraqqsgIDA61169a53dc1a9act/+vdevWzVqwYMFF+3mTkSNHWklJSdbhw4ctX19f6+DBg9bBgwctPz8/66effrKSkpKskSNHWpZlWadPn7batGljffHFF25jjBkzxnrwwQfrvI2UlBQrOTnZ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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar(g.Type, g.Accuracy)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
